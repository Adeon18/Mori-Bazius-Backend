#!/bin/bash

cd app/RegistrationLoginValidation
docker compose up --build -d
cd ./../..

cd cassandra
./run-and-configure.sh
cd ..

cd kafka
./run-cluster.sh
cd ..

cd app/game_data_service
./build.sh
./run.sh
cd ./../..

cd app/APIGetawayService
./run-api-gateway.sh
cd ./../..

cd app/SnapshotService
./build-and-run.sh
cd ./../..

cd app/StatsProcessing
docker compose up --build -d
./submit.sh
cd ./../..
