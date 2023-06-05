#!/bin/bash

docker build -f `pwd`/Dockerfile --tag game_data_service ..

CASSANDRA_ENDPOINT=${CASSANDRA_ENDPOINT:=cassandra-node-1}
CASSANDRA_PORT=${CASSANDRA_PORT:=9042}

docker run -d --network hunters-game-network --rm -p 8000:8000 --name game_data1 \
    -e CASSANDRA_ENDPOINT=${CASSANDRA_ENDPOINT} -e CASSANDRA_PORT=${CASSANDRA_PORT} \
    -e KAFKA_ADDRESS=kafka-server:9092 -e PYTHONUNBUFFERED=1 -e SERVICE_ID=1 \
    game_data_service

docker run -d --network hunters-game-network --rm --name game_data2 \
    -e CASSANDRA_ENDPOINT=${CASSANDRA_ENDPOINT} -e CASSANDRA_PORT=${CASSANDRA_PORT} \
    -e KAFKA_ADDRESS=kafka-server:9092 -e PYTHONUNBUFFERED=1 -e SERVICE_ID=2 \
    game_data_service
