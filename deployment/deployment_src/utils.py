# @Author: Webster Bei Yijie, Joey Junyu Liang
# @Date: 5/8/2020, 3:05:16 PM
# @Email: yijie.bei@duke.edu, junyu.liang@duke.edu


from torch.optim import SGD, Adam

imports = '''import torch
import torch.nn as nn
import torch.nn.functional as F
from metrics import *

'''


def get_model_class_from_config(model_config):
    model_src_with_imports = imports + model_config
    with open("model.py", "w") as f:
        f.write(model_src_with_imports)
    from model import Model
    return Model

def get_model_instance_from_config(model_config):
    model_src_with_imports = imports + model_config
    with open("model.py", "w") as f:
        f.write(model_src_with_imports)
    from model import Model
    return Model()

# TODO: Support more configurations
def get_optimizer_from_model_class(model_class, forward_net):
    if model_class.optimizer in ["SGD", "sgd", "Sgd"]:
        optimizer = SGD(forward_net.parameters(), lr = model_class.learning_rate)
    elif model_class.optimizer in ["Adam", "adam", "ADAM"]:
        optimizer = Adam(forward_net.parameters(), lr = model_class.learning_rate)
    return optimizer
