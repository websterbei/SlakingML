docker build -f ./deployment_setup/Dockerfile -t websterbei/deploymentnode:$1 ./
docker push websterbei/deploymentnode:$1