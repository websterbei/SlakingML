import torch
import numpy as np

from helper import get_model_class_from_config
from mongo import get_job_object_by_job_id
from module_factory import get_nn_module_from_model_class

training_job = get_job_object_by_job_id("5e379c4cb7a8e60b9d1434cb")
model_class = get_model_class_from_config(training_job.get("model_config"))
print(dir(model_class))
print("Learning rate is: " + str(model_class.learning_rate))
print("Optimizer is: " + model_class.optimizer)
module = get_nn_module_from_model_class(model_class)

x = np.ones((20, 784), dtype=np.float32)
y_ = np.ones((20, 1), dtype=np.float32)
tensor_x = torch.tensor(x)
tensor_y_ = torch.tensor(y_)

forward_net = module()
y = forward_net(tensor_x)
print(forward_net.loss(tensor_y_, y))
