#!/bin/bash


NETWORK_NAME="cassandra-network"
NODE1="cassandra-node-1"
NODE2="cassandra-node-2"
NODE3="cassandra-node-3"

# Launching the network
echo "Creating docker cassandra network ..."
docker network create "${NETWORK_NAME}"

sleep 1

# Launch container 1
docker run --name "${NODE1}" --network "${NETWORK_NAME}" -d cassandra:latest
echo "Node ${NODE1} launched"

# Wait till lauching node 2
echo "Waiting 1 minute till launching the next node..."
sleep 60

# Launch container 2
echo "Launching the next node..."
docker run --name ${NODE2} --network ${NETWORK_NAME} -d -e CASSANDRA_SEEDS="${NODE1}" cassandra:latest
echo "Node ${NODE2} launched"

# Wait till lauching node 3
echo "Waiting 1 minute till launching the next node..."
sleep 60

# Launch container 2
echo "Launching the next node..."
docker run --name ${NODE3} --network ${NETWORK_NAME} -d -e CASSANDRA_SEEDS="${NODE1}","${NODE2}" cassandra:latest
echo "Node ${NODE3} launched"

echo "Waiting 70 seconds till the last node connects..."
sleep 70

echo "Done"
