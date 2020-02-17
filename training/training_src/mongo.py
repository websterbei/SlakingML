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

# # TODO: Error handling
def get_job_object_by_job_id(job_id, test=False):
    if test: # Local test
        with open("model_config") as f:
            model_config = "".join(f.readlines())
        with open("data_config") as f:
            data_config = "".join(f.readlines())
        training_job = {}
        training_job["model_config"] = model_config
        training_job["data_config"] = data_config
        training_job["author_name"] = "webster"
        training_job["model_name"] = "mymodel"
        return training_job
    else:
        print("Looking up job: {}".format(job_id))
        training_job = db.jobs.find_one({"_id": ObjectId(job_id)})
        print_job_info(training_job)
        return training_job

def update_job_status(job_id, status, model_save_location = None, close_connection=True):
    update_delta = {}
    update_delta["status"] = status
    update_delta["model_save_location"] = model_save_location
    db.jobs.update_one({"_id": ObjectId(job_id)}, {"$set": update_delta})
    if close_connection:
        client.close()

def update_job_progress(job_id, metrics):
    for metric, value in metrics.items():
        db.jobs.update_one({"_id": ObjectId(job_id)}, {"$push": {"metrics.{}".format(metric): value}}, upsert=True)