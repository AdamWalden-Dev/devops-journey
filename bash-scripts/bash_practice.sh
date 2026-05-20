#!/bin/bash
read -p "Enter server name:" SERVER_NAME
read -p "Is it online or offline?" SERVER_STATUS

echo "You entered:"
echo "Server:" $SERVER_NAME
echo "Status:" $SERVER_STATUS

if [ "$SERVER_STATUS" = "online" ]; then
    echo "Server is healthy"
elif [ "$SERVER_STATUS" = "offline" ]; then
    echo "Warning: $SERVER_NAME is down"
else
    echo "Unknown status error:"
fi
