# @Author: Webster Bei Yijie, Joey Junyu Liang
# @Date: 5/8/2020, 3:04:43 PM
# @Email: yijie.bei@duke.edu, junyu.liang@duke.edu


import torch
import numpy as np
import json
import uuid
import os
import sys
import pyarrow as pa
import io

from utils import get_model_class_from_config, get_optimizer_from_model_class
from mongo import get_job_object_by_job_id
from module_factory import get_nn_module_from_model_class

from torch.utils.data import DataLoader

# TODO: needs to add tons of error checking
class Deployer():
    
    def __init__(self, job_id):
        training_job = get_job_object_by_job_id(job_id)
        self.model_class = get_model_class_from_config(training_job.get("model_config"))
        self.module = get_nn_module_from_model_class(self.model_class)()

        self.model_full_path = training_job.get("model_save_location")
        self._load_model()
     

    def _load_model(self):
        print("Loading model: " + self.model_full_path)
        try: 
            fs = pa.hdfs.connect('namenode', port=9000, driver='libhdfs3')
            f = fs.open(self.model_full_path)
            g = io.BytesIO(f.read())
            checkpoint = torch.load(g)
            f.close()
        except:
            raise Exception("Error loading module")
        
        try:
            self.module.load_state_dict(checkpoint)
            self.module.eval()
        except:
            try:
                self.module = torch.nn.DataParallel(self.module)
                self.module.load_state_dict(checkpoint)
                self.module.eval()
            except:
                raise Exception("Error loading state dict")
        
        print("Model succesfully loaded.")

    def get_prediction_(self,data_input):
        print("start predicting...")
        try:
            inarr = self.parseJson(data_input)
        except:
            raise Exception("Invalid Json input")
        input_tensor = torch.from_numpy(inarr).float();

        try:
            result = self.module.forward(input_tensor)
        except:
            raise Exception("Error when predicting")

        print('outputs:')
        print(result)
        return result

    def parseJson(self,data_input):
        try:
            ret = np.array(json.loads(data_input),dtype=np.double)
        except: 
            raise Exception("Error loading json input")
        return ret