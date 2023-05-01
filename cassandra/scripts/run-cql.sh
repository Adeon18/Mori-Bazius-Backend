#! /bin/bash

# Basically you run it like ./run-cql.sh <path-to-script-on-your-mashine> <script-destination-in-container>

docker run -v "$(pwd)"/"$1":"/script.cql" -it --network hunters-game-network --rm cassandra cqlsh cassandra-node-1 -f "/script.cql"
