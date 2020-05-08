# @Author: Webster Bei Yijie, Joey Junyu Liang
# @Date: 5/8/2020, 3:12:33 PM
# @Email: yijie.bei@duke.edu, junyu.liang@duke.edu


import json

metadata = {}
metadata["column_names"] = ["label"] + ["pixel{}".format(x) for x in range(1, 785)]
metadata["column_types"] = ["integer"] + ["float"] * 784
metadata["author_name"] = "Somebody"
metadata["dataset_name"] = "Fashion Mnist"
metadata["resource_files"] = ["fashion_mnist.csv"]

with open("metadata", "w") as f:
    json.dump(metadata, f)