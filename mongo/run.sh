#! /bin/bash

docker-compose up -d

echo "Waiting to start"

sleep 60

echo "Creating tables..."

./run-mongodb.sh
