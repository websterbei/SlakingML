import torch
import numpy as np
import json

from helper import get_model_class_from_config, get_optimizer_from_model_class
from mongo import get_job_object_by_job_id
from module_factory import get_nn_module_from_model_class

from dataset_factory import CustomInterableDataset
from torch.utils.data import DataLoader


class Trainer():
    
    def __init__(self, job_id):
        training_job = get_job_object_by_job_id(job_id)
        model_class = get_model_class_from_config(training_job.get("model_config"))
        module = get_nn_module_from_model_class(model_class)
        data_config = json.loads(training_job["data_config"])
        
        train_dataset = CustomInterableDataset(dataset_folder = data_config["train_dataset_path"])
        test_dataset = CustomInterableDataset(dataset_folder = data_config["test_dataset_path"])
        
        batch_size = data_config["batch_size"]
        self.number_of_epochs = data_config["epochs"]
        self.train_loader = DataLoader(train_dataset, batch_size = batch_size)
        self.test_loader = DataLoader(test_dataset, batch_size = batch_size)

        self.forward_net = module()
        self.optimizer = get_optimizer_from_model_class(model_class, self.forward_net)

    def _print_metrics(self, epoch_ind, batch_ind, loss):
        print("epoch: {}    batch: {}   ".format(epoch_ind, batch_ind), end='')
        print("loss: {} ".format(loss), end='')
        for metric in self.forward_net.metrics:
            print("{}: {}   ".format(metric.metric_name, metric.get_report()), end='')
        print()

    def train(self):
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

trainer = Trainer("somejobid")
trainer.train()