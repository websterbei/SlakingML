import torch
import numpy as np
import json
import uuid
import os

from utils import get_model_class_from_config, get_optimizer_from_model_class
from mongo import get_job_object_by_job_id
from module_factory import get_nn_module_from_model_class

from dataset_factory import CustomInterableDataset
from torch.utils.data import DataLoader


MODEL_SAVE_FOLDER = '/HDFS/MODELS'
DATASET_ROOT_DIR = '/HDFS/DATASETS'

# MODEL_SAVE_FOLDER = './'
# DATASET_ROOT_DIR = './'


# TODO: needs to add tons of error checking
class Trainer():
    
    def __init__(self, job_id):
        training_job = get_job_object_by_job_id(job_id)
        model_class = get_model_class_from_config(training_job.get("model_config"))
        module = get_nn_module_from_model_class(model_class)
        data_config = json.loads(training_job["data_config"])
        
        train_dataset = CustomInterableDataset(dataset_folder = os.path.join(DATASET_ROOT_DIR, data_config["train_dataset_path"]))
        test_dataset = CustomInterableDataset(dataset_folder = os.path.join(DATASET_ROOT_DIR, data_config["test_dataset_path"]))
        
        batch_size = data_config["batch_size"]
        self.number_of_epochs = data_config["epochs"]
        self.train_loader = DataLoader(train_dataset, batch_size = batch_size)
        self.test_loader = DataLoader(test_dataset, batch_size = batch_size)

        self.forward_net = module()
        self.optimizer = get_optimizer_from_model_class(model_class, self.forward_net)

        self.model_save_name = training_job["model_name"] + '-' + str(uuid.uuid1())
        self.model_save_dir = os.path.join(MODEL_SAVE_FOLDER, training_job["model_name"])
        self.full_path = os.path.join(self.model_save_dir, self.model_save_name)

    def _print_metrics(self, epoch_ind=None, batch_ind=None, loss=None):
        if epoch_ind is not None and batch_ind is not None:
            print("epoch: {}    batch: {}   ".format(epoch_ind, batch_ind), end='')
        if loss is not None:
            print("loss: {} ".format(loss), end='')
        for metric in self.forward_net.metrics:
            print("{}: {}   ".format(metric.metric_name, metric.get_report()), end='')
        print()

    def _save_model(self):
        print("Saving models......")
        if not os.path.isdir(self.model_save_dir):
            os.mkdir(self.model_save_dir)
        torch.save(self.forward_net.state_dict(), self.full_path)
        print("Model saved at {}".format(self.full_path))
        
    def train(self):
        print("Start training:")
        for epoch_ind in range(1, self.number_of_epochs+1):
            for metric in self.forward_net.metrics:
                metric.reset()
            for batch_ind, (batch_x, batch_y) in enumerate(self.train_loader):
                self.optimizer.zero_grad()
                y = self.forward_net(batch_x)
                loss = self.forward_net.loss(y, batch_y)
                self.forward_net.add_to_metric(y, batch_y)
                loss.backward()
                self.optimizer.step()
                if batch_ind%50 == 0:
                    self._print_metrics(epoch_ind, batch_ind, loss)
        print("Finished training")
        self._save_model()
    
    def test(self):
        print("Start testing:")
        for metric in self.forward_net.metrics:
            metric.reset()
        self.forward_net.eval()
        for batch_ind, (batch_x, batch_y) in enumerate(self.test_loader):
            y = self.forward_net(batch_x)
            loss = self.forward_net.loss(y, batch_y)
            self.forward_net.add_to_metric(y, batch_y)
        self._print_metrics()

job_id = os.environ.get("SLAKING_JOB_ID")
trainer = Trainer(job_id)
trainer.train()
trainer.test()