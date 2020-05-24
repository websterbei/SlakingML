# Slaking Machine Learning Platform

Authors: Webster Bei Yijie, Joey Junyu Liang
Emails: yijie.bei@duke.edu, junyu.liang@duke.edu


Machine Learning (ML), especially Deep Learning (DL), has become a new darling of technological companies. Indeed, ML has replaced traditional algorithms in performing many tasks, the most commonly known includes content recommendation, facial recognition, fraud detection and etc. The rise in popularity of ML/DL is accompanied by growth in computing power of chips developed in recent years as well as the availability of large scale datasets that are necessary for “learning”. ML algorithms have been widely deployed in the industry with the help of a variety of toolkits developed by industry leaders as well as researchers in academia.
Similar to the adoption of any significant technology in history, ML is on its way to become more beginner-friendly. In companies that now heavily rely on ML in their production environments, dummy-proof and streamlined procedures for taking raw data to actionable insights or revenue-generating functionalities were long developed and continuously optimized to ensure efficiency and reliability.


[Design Document](https://docs.google.com/document/d/1-9vEN4Kqr5zFNxTlDueuvWxmobuTrNP2cYG6La3iUx4/edit?usp=sharing)

[Demo Video with Presentation](https://drive.google.com/file/d/1CH-cYLhrcd7v0DBdD9qg_OhaoQ9hTpsg/view?usp=sharing)

## General Installation Guidelines
There are several essential components to Slaking ML Platform and they need to be run as services on the Kubernetes cluster. For now, since there is no global configuration to Slaking ML, port and service names may need to be changed in the source code to ensure that services are able to connect to each other.  

After setting up the Kubernetes cluster, you will need to run the following services not necessarily in order:
1. Hadoop containers for distributed storage. This can be done by applying YAML files under hadoop/kubernetes_configs. You may need to compile the docker images and use your own docker images instead of those specified in the YAML files.  
If you already have a Hadoop cluster externally, you will need to modify training/training_setup/base/Dockerfile to make sure that you build a docker image that is able to access your cluster. This image will be the base image for running model training and model deployment.
2. MongoDB. This is simply the vanilla mongodb service container. Make sure that you change the port and service name in backend/slaking-backend/bin/www around line 32, and training/training_src/mongodb_config.json, as well as deployment/deplotment_src/mongodb_config.json to ensure that those services connect to the correct mongodb service in your Kubernetes cluster.
3. Slaking backend. Slaking backend can be deployed by simply deploying the docker image built using the backend/backend_setup/Dockerfile. Before compiling the backend docker image, you need to update the backend/slaking-backend/routes/kubernetes_config.yml to make sure backend is authorized to access your Kubernetes cluster APIs. Note that Slaking backend needs to be exposed publicly to outside the cluster. Take note of this publicly accessible endpoint and modify frontend/slaking-frontend/src/configurations.js to make sure the frontend is accessing the correct backend API.
4. Slaking frontend. Slaking frontend can be similarly set up by deploying the docker image built using the frontend/frontend_setup/Dockerfile. This also needs to be exposed externally.
