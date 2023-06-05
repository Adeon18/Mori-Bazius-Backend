#!/bin/bash
while ! curl -f -s http://consul:8500/v1/status/leader | grep "[0-9]:[0-9]"; do
  sleep 2
done
consul kv put "map-name" "logged-users"