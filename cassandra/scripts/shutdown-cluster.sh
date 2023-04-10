#! /bin/bash

NETWORK_NAME="cassandra-network"
NODE1="cassandra-node-1"
NODE2="cassandra-node-2"
NODE3="cassandra-node-3"

# Shutdown NODE1
if [ "$(docker ps -a | grep ${NODE1})" ]; then
    echo "Docker container with name ${NODE1} exists, stopping and deleting..."
    docker stop "${NODE1}"
    docker rm "${NODE1}"
fi

# Shutdown NODE2
if [ "$(docker ps -a | grep "${NODE2}")" ]; then
    echo "Docker container with name ${NODE2} exists, stopping and deleting..."
    docker stop "${NODE2}"
    docker rm "${NODE2}"
fi

# Shutdown NODE3
if [ "$(docker ps -a | grep "${NODE3}")" ]; then
    echo "Docker container with name ${NODE3} exists, stopping and deleting..."
    docker stop "${NODE3}"
    docker rm "${NODE3}"
fi

# SHutdown network
if [ "$(docker network ls | grep "${NETWORK_NAME}")" ]; then
    echo "Docker network with name ${NETWORK_NAME} exists, stopping and deleting..."
    docker network rm "${NETWORK_NAME}"
fi

