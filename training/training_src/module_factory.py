import torch.nn as nn

def nn_module_init(self):
    super(self.__class__, self).__init__()
    self.initialize()

def get_nn_module_from_model_class(model_class):
    nn_module = type("ModelModule", (nn.Module, ), {
        "__init__": nn_module_init,
        "initialize": model_class.initialize,
        "forward": model_class.forward,
        "loss": model_class.loss,
        "add_to_metric": model_class.add_to_metric
        })

    return nn_module