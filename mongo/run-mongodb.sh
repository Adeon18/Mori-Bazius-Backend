docker run -v "./init_mongodb.sh:/docker-entrypoint-initdb.d/init_mongodb.sh" -it --network hunters-game-network --rm mongo bash "/docker-entrypoint-initdb.d/init_mongodb.sh" -e MONGODB_HOST=mongodb
