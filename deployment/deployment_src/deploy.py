import torch
import numpy as np
import json
import uuid
import os
import sys
training_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))+ '/training/training_src/')
sys.path.append(training_dir)


from utils import get_model_class_from_config, get_optimizer_from_model_class
from mongo import get_job_object_by_job_id
from module_factory import get_nn_module_from_model_class


# from prepare_data import DeploymentInputDataset
from torch.utils.data import DataLoader



# MODEL_SAVE_FOLDER = '/HDFS/MODELS'
# DATASET_ROOT_DIR = '/HDFS/DATASETS'

MODEL_SAVE_FOLDER = './'
RESULT_SAVE_FOLDER = './DeploymentResult'
DATASET_ROOT_DIR = './'
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))


# TODO: needs to add tons of error checking
class Deployer():
    
    def __init__(self, job_id):
        training_job = get_job_object_by_job_id(job_id,test=True)
        self.model_class = get_model_class_from_config(training_job.get("model_config"))
        self.module = get_nn_module_from_model_class(self.model_class)()
        
        # self.result_save_name = 'deployment-'+training_job["model_name"] + '-' + str(uuid.uuid1())
        # self.result_save_dir = os.path.join(RESULT_SAVE_FOLDER, training_job["model_name"])
        # self.result_full_path = os.path.join(self.result_save_dir, self.result_save_name)

        # TODO: how to get the full model save name?
        self.model_save_name = "mymodel-d943fa98-4c49-11ea-ab7a-acde48001122"
        self.model_save_dir = "./"
        self.model_full_path = os.path.join(THIS_FOLDER, self.model_save_name)
        print(self.model_full_path)

        self._load_model()
     

    def _load_model(self):
        print("Loading model: "+self.model_save_name)
        try: 
            checkpoint = torch.load(self.model_full_path)
        except:
            raise Exception("Error loading module")
        
        try:
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
    
# deployer = Deployer("somejobid")
# with open("deployment_input",'r') as f:
#       line_raw = f.readline().rstrip()
#       output = deployer.get_prediction_(line_raw)

    
    