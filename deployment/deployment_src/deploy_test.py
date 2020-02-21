import requests

input_data = {'job_id':'somejobid'} 
resp = requests.post('http://127.0.0.1:5000/deploy',json=input_data )

with open("deployment_input",'r') as f:
      line_raw = f.readline().rstrip()
predict_data = {'data':line_raw}
resp = requests.post('http://127.0.0.1:5000/predict',json=predict_data )
                    
