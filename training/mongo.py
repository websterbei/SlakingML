from pymongo import MongoClient
import pprint
from bson.objectid import ObjectId

import json

with open("mongodb_config.json") as f:
    mongodb_config = json.load(f)
client = MongoClient(mongodb_config["url"])
db = client.jobs

def print_job_info(training_job):
    model_config = training_job.get("model_config")
    data_config = training_job.get("data_config")
    author_name = training_job.get("author_name")
    model_name = training_job.get("model_name")
    print("Model Name: \n" + model_name)
    print("Author Name: \n" + author_name)
    print("Data Config: ")
    print(data_config)
    print("Model Config: ")
    print(model_config)

# TODO: Error handling
def get_job_object_by_job_id(job_id):
    print("Looking up job: {}".format(job_id))
    training_job = db.jobs.find_one({"_id": ObjectId(job_id)})
    client.close()
    print_job_info(training_job)
    return training_job

# Local test
def get_configs_by_job_id(job_id):
    with open("model_config") as f:
        model_config = "".join(f.readlines())
    with open("data_config") as f:
        data_config = json.load(f)
    training_job = {}
    training_job["model_config"] = model_config
    training_job["data_config"] = data_config
    training_job["author_name"] = "webster"
    training_job["model_name"] = "my model"
    return training_job