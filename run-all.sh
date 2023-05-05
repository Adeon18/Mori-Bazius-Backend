#!/bin/bash

cd cassandra
./run-and-configure.sh
cd ..

cd kafka
./run-cluster.sh
cd ..

cd app/game_data_service
./run.sh
cd ./../..

cd app/APIGetawayService
./run-api-gateway.sh
cd ./../..

cd app/RegistrationLoginValidation
docker compose up --build -d
cd ./../..
