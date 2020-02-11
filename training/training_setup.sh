docker build -f ./training_setup/trainnode/Dockerfile -t websterbei/trainnode:v1 ./
docker run -it --privileged --network="slaking_network" --env SLAKING_JOB_ID=$1 websterbei/trainnode:v1