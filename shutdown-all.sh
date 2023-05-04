#!/bin/sh

cd kafka
./shutdown-cluster.sh
cd ..

cd app
cd game_data_service
./stop.sh
cd ./../..

cd app
cd APIGetawayService
./stop.sh
cd ./../..

cd app
cd RegistrationLoginValidation
docker compose down
cd ./../..

cd cassandra
./stop.sh
cd ..