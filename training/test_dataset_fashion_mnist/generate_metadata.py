import json

metadata = {}
metadata["column_names"] = ["label"] + ["pixel{}".format(x) for x in range(1, 785)]
metadata["column_types"] = ["integer"] + ["float"] * 784
metadata["author_name"] = "Somebody"
metadata["dataset_name"] = "Fashion Mnist"
metadata["resource_files"] = ["fashion_mnist.csv"]

with open("metadata", "w") as f:
    json.dump(metadata, f)