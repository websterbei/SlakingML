import torch
import torch.distributed as dist
from torch.nn.parallel import DistributedDataParallel
import numpy as np
import json
import uuid
import os
import sys
import pyarrow as pa

from utils import get_model_class_from_config, get_optimizer_from_model_class
from mongo import get_job_object_by_job_id, update_job_status, update_job_progress
from module_factory import get_nn_module_from_model_class

from dataset_factory import CustomIterableDataset, CustomDistributedIterableDataset
from torch.utils.data import DataLoader


# TODO: needs to add tons of error checking
class Trainer():
    
    def __init__(self, job_id, local_test=False, use_pyarrow=True):
        self.job_id = job_id
        self.local_test = local_test
        # Lookup training job object from Mongo database, mongo database configuration in mongodb_config.json
        self.training_job = get_job_object_by_job_id(job_id, test=local_test)
        # Get the customized model class from the config file
        self.model_class = get_model_class_from_config(self.training_job.get("model_config"))
        # Construct pytorch module from the model class
        self.module = get_nn_module_from_model_class(self.model_class)
        
        # Get data config for the training job
        self.data_config = json.loads(self.training_job["data_config"])
        
        # Setup pyarrow for HDFS file access or fs for local filesystem access
        self.use_pyarrow = use_pyarrow
        if use_pyarrow:
            self.fs = pa.hdfs.connect('namenode', port=9000, driver='libhdfs3')
        train_dataset = CustomIterableDataset(dataset_folder = os.path.join(DATASET_ROOT_DIR, self.data_config["train_dataset_path"]), 
                                              label_columns = self.data_config["label_columns"] if "label_columns" in self.data_config else ["label"],
                                              feature_columns = self.data_config["feature_columns"] if "feature_columns" in self.data_config else None,
                                              use_pyarrow = use_pyarrow)
        test_dataset = CustomIterableDataset(dataset_folder = os.path.join(DATASET_ROOT_DIR, self.data_config["test_dataset_path"]),
                                             label_columns = self.data_config["label_columns"] if "label_columns" in self.data_config else ["label"],
                                             feature_columns = self.data_config["feature_columns"] if "feature_columns" in self.data_config else None,
                                             use_pyarrow=use_pyarrow)

        self.batch_size = self.data_config["batch_size"]
        self.number_of_epochs = self.data_config["epochs"]
        self.train_loader = DataLoader(train_dataset, batch_size = self.batch_size)
        self.test_loader = DataLoader(test_dataset, batch_size = self.batch_size)

        # Create net
        self.forward_net = self.module()
        # Create optimizer
        self.optimizer = get_optimizer_from_model_class(self.model_class, self.forward_net)

        # Set up checkpoint save info
        self.model_save_name = self.training_job["model_name"] + '-' + str(uuid.uuid1())
        self.model_save_dir = os.path.join(MODEL_SAVE_FOLDER, self.training_job["model_name"])
        self.full_path = os.path.join(self.model_save_dir, self.model_save_name)

        # Update job status
        if not self.local_test:
            update_job_status(self.job_id, "in progress", close_connection=False)

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
        if self.use_pyarrow:
            if not self.fs.exists(self.model_save_dir):
                self.fs.mkdir(self.model_save_dir)
            with self.fs.open(self.full_path, 'wb') as f:
                torch.save(self.forward_net.state_dict(), f)
        else:
            if not os.path.isdir(self.model_save_dir):
                os.mkdir(self.model_save_dir)
            torch.save(self.forward_net.state_dict(), self.full_path)
        print("Model saved at {}".format(self.full_path))
        if not self.local_test:
            update_job_status(self.job_id, "successful", self.full_path)
        print("Job status synchronized")

    def _update_job_progress(self, loss=None):
        if not self.local_test:
            metric_reports = {}
            metric_reports["loss"] = loss.detach().item()
            for metric in self.forward_net.metrics:
                metric_reports[metric.metric_name] = metric.get_report()
            update_job_progress(self.job_id, metric_reports)

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
                self._update_job_progress(loss)
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

class DistributedTrainer(Trainer):
    
    def __init__(self, job_id, rank, world_size, master_address, master_port, local_test=False, use_pyarrow=True):
        super().__init__(job_id, local_test=local_test, use_pyarrow=use_pyarrow)
        self.world_size = world_size
        self.rank = rank
        self.master_address = master_address
        self.master_port = master_port

        train_dataset = CustomDistributedIterableDataset(dataset_folder = os.path.join(DATASET_ROOT_DIR, self.data_config["train_dataset_path"]), 
                                              label_columns = self.data_config["label_columns"] if "label_columns" in self.data_config else ["label"],
                                              feature_columns = self.data_config["feature_columns"] if "feature_columns" in self.data_config else None,
                                              use_pyarrow = use_pyarrow,
                                              rank = self.rank,
                                              world_size=self.world_size)
        test_dataset = CustomIterableDataset(dataset_folder = os.path.join(DATASET_ROOT_DIR, self.data_config["test_dataset_path"]),
                                             label_columns = self.data_config["label_columns"] if "label_columns" in self.data_config else ["label"],
                                             feature_columns = self.data_config["feature_columns"] if "feature_columns" in self.data_config else None,
                                             use_pyarrow=use_pyarrow)
        
        self.train_loader = DataLoader(train_dataset, batch_size = self.batch_size)
        self.test_loader = DataLoader(test_dataset, batch_size = self.batch_size)

        # Set up distributed training environment
        self._distributed_training_setup()

        # Create distributed net
        _forward_net = self.module()
        self.forward_net = DistributedDataParallel(self.module())
        self.forward_net.metrics = _forward_net.metrics
        self.forward_net.loss = _forward_net.loss
        self.forward_net.add_to_metric = _forward_net.add_to_metric
        # Create optimizer
        self.optimizer = get_optimizer_from_model_class(self.model_class, self.forward_net)

        # Set up checkpoint save info
        self.model_save_name = self.training_job["model_name"] + '-' + str(uuid.uuid1())
        self.model_save_dir = os.path.join(MODEL_SAVE_FOLDER, self.training_job["model_name"])
        self.full_path = os.path.join(self.model_save_dir, self.model_save_name)

        # Update job status, only the master node will update job status
        if rank == 0:
            update_job_status(self.job_id, "in progress", close_connection=False)
    
    def _distributed_training_setup(self):
        # Using env:/ as the default init method, master container ip and port are needed
        os.environ['MASTER_ADDR'] = self.master_address
        os.environ['MASTER_PORT'] = str(self.master_port)

        # Initialize process group, using gloo backend
        dist.init_process_group("gloo", rank=self.rank, world_size=self.world_size)
        
        # This ensures that local copies of weights across machines are initialized to be the same
        torch.manual_seed(1234)

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
                # Only master node will update metric info
                if self.rank == 0:
                    self._update_job_progress(loss)
        print("Finished training")
        # Only master node will save model
        if self.rank == 0:
            self._save_model()


if "-distributed" in sys.argv:
    rank = int(os.environ.get("SLAKING_RANK"))
    world_size = int(os.environ.get("SLAKING_WORLD_SIZE"))
    master_address = os.environ.get("SLAKING_MASTER_ADDRESS")
    master_port = int(os.environ.get("SLAKING_MASTER_PORT"))
    if "-test" in sys.argv:
        MODEL_SAVE_FOLDER = '../'
        DATASET_ROOT_DIR = '../'
        job_id = sys.argv[-1]
        if "-local" in sys.argv:
            trainer = DistributedTrainer(job_id, rank, world_size, master_address, master_port, local_test=True, use_pyarrow=False)
        else:
            trainer = DistributedTrainer(job_id, rank, world_size, master_address, master_port, use_pyarrow=False)
    else:
        MODEL_SAVE_FOLDER = '/MODELS'
        DATASET_ROOT_DIR = '/DATASETS'
        job_id = os.environ.get("SLAKING_JOB_ID")
        trainer = DistributedTrainer(job_id, rank, world_size, master_address, master_port, use_pyarrow=True)
    trainer.train()
    # Perform validation only on master node
    if rank == 0:
        trainer.test()
else:
    if "-test" in sys.argv:
        MODEL_SAVE_FOLDER = '../'
        DATASET_ROOT_DIR = '../'
        job_id = sys.argv[-1]
        if "-local" in sys.argv:
            trainer = Trainer(job_id, local_test=True, use_pyarrow=False)
        else:
            trainer = Trainer(job_id, use_pyarrow=False)
    else:
        MODEL_SAVE_FOLDER = '/MODELS'
        DATASET_ROOT_DIR = '/DATASETS'
        job_id = os.environ.get("SLAKING_JOB_ID")
        trainer = Trainer(job_id, use_pyarrow=True)
    trainer.train()
    trainer.test()