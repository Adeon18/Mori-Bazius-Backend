#!/bin/bash

CASSANDRA_ENDPOINT=${CASSANDRA_ENDPOINT:=cassandra-node-1}
CASSANDRA_PORT=${CASSANDRA_PORT:=9042}

docker run -d --rm --network cassandra-network -p 8000:8000 --name game_data \
    -e CASSANDRA_ENDPOINT=${CASSANDRA_ENDPOINT} -e CASSANDRA_PORT=${CASSANDRA_PORT} game_data_service