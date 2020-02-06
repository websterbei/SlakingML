import numpy as np
import torch
from torch.utils.data import IterableDataset
import json
import os

# TODO: Error handling, change to multiworker version (only possible when multiple resource files exist?), handle image type
class CustomInterableDataset(IterableDataset):
    
    def __init__(self, dataset_folder, label_columns=["label"], feature_columns=None):
        # read metadata
        metadata = None
        try:
            with open(os.path.join(dataset_folder, "metadata")) as f:
                metadata = json.load(f)
        except:
            raise Exception("Did not find metadata file in given folder")
        # basic error checking
        if (metadata.get("column_names", None) is None) or (len(metadata.get("column_names")) == 0) \
            or (metadata.get("column_types", None) is None) or (len(metadata.get("column_types")) == 0) \
            or (len(metadata.get("column_names")) != len(metadata.get("column_types"))):
            raise Exception("metadata incorrect")
        
        self.resource_files = [os.path.join(dataset_folder, resource_file) for resource_file in metadata["resource_files"]]

        # if label_columns was set to None, no label is retrieved
        if label_columns is None:
            self.label_columns = None
            self.label_types = None
        else:
            self.label_columns = [metadata["column_names"].index(label_name) for label_name in label_columns]
            self.label_types = [metadata["column_types"][ind] for ind in self.label_columns]

        # if feature_columns is set to None, then all columns except the label columns are retrieved
        if feature_columns is None:
            selected_features = list(metadata["column_names"])
            if self.label_columns is not None:
                for label_ind in self.label_columns:
                    del selected_features[label_ind]
        else:
            selected_features = feature_columns
        self.feature_columns = [metadata["column_names"].index(feature_name) for feature_name in selected_features]
        self.feature_types = [metadata["column_types"][ind] for ind in self.feature_columns]

    def _load_images(self, folder, filename):
        pass

    def _cast(self, string_value, dtype):
        if dtype == "integer":
            return int(string_value)
        elif dtype == "float":
            return float(string_value)
        elif dtype == "image":
            pass
        else:
            raise Exception("Unsupported datatype: " + dtype)

    def __iter__(self):
        for resource_file in self.resource_files:
            with open(resource_file) as f:
                line_raw = f.readline().rstrip()
                while line_raw:
                    line = line_raw.split(",")
                    features = [self._cast(line[ind], dtype) for ind, dtype in zip(self.feature_columns, self.feature_types)]
                    if self.label_columns is not None:
                        labels = [self._cast(line[ind], dtype) for ind, dtype in zip(self.label_columns, self.label_types)]
                        yield np.array(features, dtype=np.float32), np.array(labels)
                    else:
                        yield np.array(features, dtype=np.float32)
                    line_raw = f.readline().rstrip()