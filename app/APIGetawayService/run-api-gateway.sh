#!/bin/bash

docker build . -t api-gateway:1.0

echo "Running write client..."

docker run --network kafka-network -p 8080:8080 --rm api-gateway:1.0

