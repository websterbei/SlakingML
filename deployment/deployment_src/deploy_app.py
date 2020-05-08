# @Author: Webster Bei Yijie, Joey Junyu Liang
# @Date: 5/8/2020, 3:01:09 PM
# @Email: yijie.bei@duke.edu, junyu.liang@duke.edu


import io
import json
import os

from deploy import Deployer
from flask import Flask, jsonify, request


_my_deployer = None


deploy_app = Flask(__name__)

@deploy_app.route('/deploy', methods=['POST'])
def deploy():
    if request.method == 'POST':
        request_data = request.json
        job_id = request_data["job_id"]
        assert(job_id is not None),"Missing job id"
        print("job id:")
        print(job_id)
        global _my_deployer 
        try:
            _my_deployer = Deployer(job_id)
        except:
            print("Error init")
            return "Error"
        return "Success"

@deploy_app.route('/', methods=['GET'])
def index():
    return "Running"
      
@deploy_app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        if _my_deployer is None:
            return "Error"
        data = request.json #should be in json string format
        try:
            result = _my_deployer.get_prediction_(data['data'])
        except:
            print("Error occurred when getting prediction")
            return ""
        result_json = json.dumps(result.detach().numpy().tolist())
        print("returns json string to client:")
        print(result_json)
        return result_json


if __name__ == '__main__':
    job_id = os.environ.get("SLAKING_JOB_ID")
    try:
        _my_deployer = Deployer(job_id)
    except:
        print("Error init")
    deploy_app.run(host='0.0.0.0', port=5000)