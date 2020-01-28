## Instruction for building an image with the backend code and running it inside a container

```
cd image_build_backup
# build docker image with backend code from the folder /backend/slaking-backend
make -B backendnode
# the above step should create a docker image locally, name and tagged by websterbei/slaking-backendnode:v1
docker run -p 8080:3000 websterbei/slaking-backendnode:v1
```

After running the above command, you will see no output at all, but you should be able to visit localhost:8080 and see some output