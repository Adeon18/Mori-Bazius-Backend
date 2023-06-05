#!/bin/bash
set -e

MONGODB_HOST=mongodb
MONGODB_PORT=27017
DATABASE_NAME="guilds"

mongosh "${MONGODB_HOST}:${MONGODB_PORT}/${DATABASE_NAME}" \
  --eval "db.createCollection('guilds')" \
  --eval "db.createCollection('members')"

echo "Created guilds and members tables."
