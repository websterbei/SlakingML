docker build -f ./training_setup/trainnode/Dockerfile -t websterbei/trainnode:v1 ./
docker push websterbei/trainnode:v1
kubectl apply -f gcloud_training_job_deployment.yml