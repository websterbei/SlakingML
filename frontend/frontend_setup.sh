cd slaking-frontend && npm run build
cd ..
docker build -f ./frontend_setup/Dockerfile -t websterbei/slaking-frontendnode:v1 ./
docker-compose up
