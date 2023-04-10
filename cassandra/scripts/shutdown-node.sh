#! /bin/bash

NETWORK_NAME="cassandra-network"
NODE1="cassandra-node-1"

# Shutdown NODE1
if [ "$(docker ps -a | grep ${NODE1})" ]; then
    echo "Docker container with name ${NODE1} exists, stopping and deleting..."
    docker stop "${NODE1}"
    docker rm "${NODE1}"
fi


# SHutdown network
if [ "$(docker network ls | grep "${NETWORK_NAME}")" ]; then
    echo "Docker network with name ${NETWORK_NAME} exists, stopping and deleting..."
    docker network rm "${NETWORK_NAME}"
fi

