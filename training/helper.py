imports = '''import torch
import torch.nn as nn
import torch.nn.functional as F

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