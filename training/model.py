import torch
import torch.nn as nn
import torch.nn.functional as F

class Model():
    optimizer = "adam"
    learning_rate = 0.0001
    epochs = 10
    
    # initialize method is called once before forward and loss methods are called
    def initialize(self):
        self.linear1 = nn.Linear(784, 100)
        self.linear2 = nn.Linear(100, 50)
        self.linear3 = nn.Linear(50, 10)
        self.lossFn = nn.CrossEntropyLoss()

    # y_: label
    # y: model output from forward method
    def loss(self, y, y_):
        return self.lossFn(y, y_.view(-1))

    def forward(self, x):
        xx = self.linear1(x)
        xx = F.relu(xx)
        xx = self.linear2(xx)
        xx = F.relu(xx)
        xx = self.linear3(xx)
        return F.softmax(xx)