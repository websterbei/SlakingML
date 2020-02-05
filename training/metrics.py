import numpy as np

class Metric_Accuracy():
    def __init__(self):
        self.metric_name = "Accuracy"
        self.label_list = []
        self.prediction_list = []

    def reset(self):
        self.label_list = []
        self.prediction_list = []

    def append(self, y, y_):
        y = y.detach().numpy().tolist()
        y_ = y_.detach().numpy().tolist()
        if len(y) != len(y_):
            raise Exception("Label and prediction shape unmatch!")
        self.label_list += y_
        self.prediction_list += y

    def get_report(self):
        label_list = np.array(self.label_list)
        prediction_list = np.array(self.prediction_list)
        num_true_positive = float((label_list==prediction_list).sum())
        num_total = len(label_list)
        return num_true_positive/num_total
        

