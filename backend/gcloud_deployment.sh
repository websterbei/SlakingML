docker build -f ./backend_setup/Dockerfile -t gcr.io/ece496-ml-system/slaking-backendnode:$1 ./
docker push gcr.io/ece496-ml-system/slaking-backendnode:$1
kubectl set image deployment/slaking-backend slaking-backendnode=gcr.io/ece496-ml-system/slaking-backendnode:$1
