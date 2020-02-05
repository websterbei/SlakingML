import torch
import numpy as np

from helper import get_model_class_from_config, get_optimizer_from_model_class
from mongo import get_job_object_by_job_id
from module_factory import get_nn_module_from_model_class

from dataset_factory import CustomInterableDataset
from torch.utils.data import DataLoader

training_job = get_job_object_by_job_id("5e379c4cb7a8e60b9d1434cb")
model_class = get_model_class_from_config(training_job.get("model_config"))
print("Learning rate is: " + str(model_class.learning_rate))
print("Optimizer is: " + model_class.optimizer)
module = get_nn_module_from_model_class(model_class)

dataset = CustomInterableDataset(dataset_folder = "./test_dataset_fashion_mnist")
loader = DataLoader(dataset, batch_size = 10)

forward_net = module()
optimizer = get_optimizer_from_model_class(model_class, forward_net)
number_of_epochs = model_class.epochs

for _ in range(number_of_epochs):
    for batch_ind, (batch_x, batch_y) in enumerate(loader):
        optimizer.zero_grad()
        y = forward_net(batch_x)
        loss = forward_net.loss(y, batch_y)
        loss.backward()
        optimizer.step()
        if batch_ind % 50 == 0:
            print(loss)
