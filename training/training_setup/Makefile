build:
	docker build -t websterbei/pytorch-base:v1 ./base
	docker build -t websterbei/pytorch-trainnode:v1 ./trainnode

base: ./base/Dockerfile
	docker build -t websterbei/pytorch-base:v1 ./base

trainnode: ./trainnode/Dockerfile
	docker build -t websterbei/pytorch-trainnode:v1 ./trainnode