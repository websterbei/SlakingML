# @Author: Webster Bei Yijie, Joey Junyu Liang
# @Date: 5/8/2020, 3:12:31 PM
# @Email: yijie.bei@duke.edu, junyu.liang@duke.edu


import numpy as np

img = np.load("train_images.npy")
label = np.load("train_labels.npy")

with open("fashion_mnist.csv", "w") as f:
    for i in range(img.shape[0]):
        temp = [label[i]] + img[i].tolist()
        temps = [str(x) for x in temp]
        f.write(",".join(temps) + "\n")