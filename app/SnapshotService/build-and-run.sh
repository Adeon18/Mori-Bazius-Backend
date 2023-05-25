#!/bin/bash

CASSANDRA_ENDPOINT=${CASSANDRA_ENDPOINT:=cassandra-node-1}
CASSANDRA_PORT=${CASSANDRA_PORT:=9042}

docker build -f `pwd`/Dockerfile .. -t snapshot_service:1.0

docker run --rm --network hunters-game-network -p 9010:9010 --name snapshot_service \
    -e CASSANDRA_ENDPOINT=${CASSANDRA_ENDPOINT} -e CASSANDRA_PORT=${CASSANDRA_PORT} \
    -e PYTHONUNBUFFERED=1 --rm snapshot_service:1.0