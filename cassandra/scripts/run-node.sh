#! /bin/bash


NETWORK_NAME="cassandra-network"
NODE1="cassandra-node-1"

# Launching the network
echo "Creating docker cassandra network ..."
docker network create "${NETWORK_NAME}"

sleep 1

# Launch container 1
docker run --name "${NODE1}" --network "${NETWORK_NAME}" -p 9042:9042 -d cassandra:latest
echo "Node ${NODE1} launched"

# Wait till lauching node 2
echo "Waiting 30 seconds for all configurations to be completed..."
sleep 30

