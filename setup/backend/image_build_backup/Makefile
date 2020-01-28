build:
	docker build -t websterbei/nodejs-base:v1 ./base
	docker build -f ./backendnode/Dockerfile -t websterbei/slaking-backendnode:v1 ../../../

base:
	docker build -t websterbei/nodejs-base:v1 ./base

backendnode:
	docker build -f ./backendnode/Dockerfile -t websterbei/slaking-backendnode:v1 ../../../