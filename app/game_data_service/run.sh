#!/bin/bash

CASSANDRA_ENDPOINT=${CASSANDRA_ENDPOINT:=cassandra-node-1}
CASSANDRA_PORT=${CASSANDRA_PORT:=9042}

docker run -d --rm --network hunters-game-network -p 8000:8000 --name game_data \
    -e CASSANDRA_ENDPOINT=${CASSANDRA_ENDPOINT} -e CASSANDRA_PORT=${CASSANDRA_PORT} \
    -e KAFKA_ADDRESS=kafka-server:9092 -e PYTHONUNBUFFERED=1 \
    game_data_service
