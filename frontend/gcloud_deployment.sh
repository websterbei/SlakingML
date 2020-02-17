cd slaking-frontend && npm run build
cd ..
docker build -f ./frontend_setup/Dockerfile -t gcr.io/ece496-ml-system/slaking-frontendnode:$1 ./
docker push gcr.io/ece496-ml-system/slaking-frontendnode:$1
kubectl set image deployment/slaking-frontend slaking-frontendnode=gcr.io/ece496-ml-system/slaking-frontendnode:$1
