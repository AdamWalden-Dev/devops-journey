#!/bin/bash

SERVERS=("server1" "server2" "server3" "server4")

for SERVER in "${SERVERS[@]}"; do
    echo "Checking server: $SERVER"
done
echo "All servers checked"