#!/bin/bash

docker build -f `pwd`/Dockerfile .. -t api-gateway:1.0

echo "Running write client..."

docker run --network kafka-network -p 9000:9000 --rm api-gateway:1.0
