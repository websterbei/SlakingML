import torch
import torch.nn as nn
import torch.nn.functional as F

class Model():
    optimizer = "adam"
    learning_rate = 0.0001
    
    # initialize method is called once before forward and loss methods are called
    def initialize(self):
        self.linear1 = nn.Linear(784, 100)
        self.linear2 = nn.Linear(100, 1)

    # y_: label
    # y: model output from forward method
    def loss(self, y_, y):
        return torch.mean((y-y_) * (y-y_))

    def forward(self, x):
        xx = self.linear1(x)
        return self.linear2(xx)