# @Author: Webster Bei Yijie, Joey Junyu Liang
# @Date: 5/8/2020, 3:05:05 PM
# @Email: yijie.bei@duke.edu, junyu.liang@duke.edu


import torch.nn as nn

def nn_module_init(self):
    super(self.__class__, self).__init__()
    self.initialize()

def get_nn_module_from_model_class(model_class):
    ModelModule = type("ModelModule", (nn.Module, ), {
        "__init__": nn_module_init,
        "initialize": model_class.initialize,
        "forward": model_class.forward,
        "loss": model_class.loss,
        "add_to_metric": model_class.add_to_metric
        })
    ModelModule.__module__ = '__main__'
    return ModelModule