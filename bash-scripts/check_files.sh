#!/bin/bash

if [ -f "servers.csv" ] && [ -f "day3.py" ]; then
    echo "Both files found, running monitor"
    python3 day3.py
else 
    echo "Canot run monitor, files missing"
fi