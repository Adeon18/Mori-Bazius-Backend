#!/bin/bash

# Set the paths and variables
PYSPARK_SCRIPT=`pwd`/stats_processing.py
SPARK_MASTER="spark://spark:7077"

docker run --rm --network hunters-game-network --name hunters-spark-submit -v ${PYSPARK_SCRIPT}:/stats_processing.py bitnami/spark:3.3 \
    /bin/bash -c "spark-submit --packages com.datastax.spark:spark-cassandra-connector_2.12:3.3.0\
    --master $SPARK_MASTER /stats_processing.py"
