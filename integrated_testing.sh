docker network create --driver=bridge slaking_network
cd backend && ./backend_setup.sh &
cd -
cd frontend && ./frontend_setup.sh &
cd -

