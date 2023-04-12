#! /bin/bash

# Run the cluster via docker compose, wait 2 minutes and create the needed tables 

docker-compose up -d

echo "Waiting for the last node to connect..."

sleep 130

echo "Creating tables..."

./scripts/run-cql.sh ./cql/create_tables.cql

