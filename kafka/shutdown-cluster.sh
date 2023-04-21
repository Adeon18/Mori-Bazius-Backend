#! /bin/bash

NETWORK_NAME="kafka-network"
ZOOKEPER_NAME="zookeeper-server"
KAFKA_NAME="kafka-server"

# Shutdown NODE1
if [ "$(docker ps -a | grep ${ZOOKEPER_NAME})" ]; then
    echo "Docker container with name ${ZOOKEPER_NAME} exists, stopping and deleting..."
    docker stop "${ZOOKEPER_NAME}"
    docker rm "${ZOOKEPER_NAME}"
fi

# Shutdown NODE2
if [ "$(docker ps -a | grep ${KAFKA_NAME})" ]; then
    echo "Docker container with name ${KAFKA_NAME} exists, stopping and deleting..."
    docker stop "${KAFKA_NAME}"
    docker rm "${KAFKA_NAME}"
fi

# SHutdown network
if [ "$(docker network ls | grep "${NETWORK_NAME}")" ]; then
    echo "Docker network with name ${NETWORK_NAME} exists, stopping and deleting..."
    docker network rm "${NETWORK_NAME}"
fi

