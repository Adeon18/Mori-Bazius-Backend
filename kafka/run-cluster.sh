#! /bin/bash


NETWORK_NAME="kafka-network"
ZOOKEPER_NAME="zookeeper-server"
KAFKA_NAME="kafka-server"
TOPIC_NAME1="game-data"
TOPIC_NAME2="game-stats"

# Launching the network
echo "Creating docker kafka network ..."
docker network create "${NETWORK_NAME}"

sleep 1

# Launch container 1
docker run -d --name "${ZOOKEPER_NAME}" --network "${NETWORK_NAME}" -e ALLOW_ANONYMOUS_LOGIN=yes bitnami/zookeeper:latest
echo "Node ${ZOOKEPER_NAME} launched"

echo "Waiting 5 second till ${KAFKA_NAME} launch..."
sleep 5

# Launch container 2
docker run -d --name "${KAFKA_NAME}" --network "${NETWORK_NAME}" -e ALLOW_PLAINTEXT_LISTENER=yes -e KAFKA_CFG_ZOOKEEPER_CONNECT=zookeeper-server:2181 bitnami/kafka:latest
echo "Node ${KAFKA_NAME} launched"

echo "Waiting 5 seconds before topic creation..."
sleep 5

# Create topic 1 - game data
docker run -it --rm --network "${NETWORK_NAME}" -e KAFKA_CFG_ZOOKEEPER_CONNECT="${ZOOKEPER_NAME}":2181 bitnami/kafka:latest kafka-topics.sh --create  --bootstrap-server ${KAFKA_NAME}:9092 --replication-factor 1 --partitions 3 --topic "${TOPIC_NAME1}"
echo "Created Kafka topic ${TOPIC_NAME1}"

sleep 1

# Create topic 2 - game stats
docker run -it --rm --network "${NETWORK_NAME}" -e KAFKA_CFG_ZOOKEEPER_CONNECT="${ZOOKEPER_NAME}":2181 bitnami/kafka:latest kafka-topics.sh --create  --bootstrap-server ${KAFKA_NAME}:9092 --replication-factor 1 --partitions 3 --topic "${TOPIC_NAME2}"
echo "Created Kafka topic ${TOPIC_NAME2}"

