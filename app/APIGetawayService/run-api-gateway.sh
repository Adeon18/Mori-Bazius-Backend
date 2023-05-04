#!/bin/bash

docker build -f `pwd`/Dockerfile .. -t api-gateway:1.0

echo "Running write client..."

docker run -d --network hunters-game-network --name api-gateway-service -p 9000:9000 --rm api-gateway:1.0
