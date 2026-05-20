#!/bin/bash

CSV_FILE="servers.csv"
SCRIPT="monitor_log.py"

if [ -f "$SCRIPT" ] && [ -f "$CSV_FILE" ]; then
    python3 $SCRIPT
    if [ $? -eq 0 ]; then
        echo "All clear, committing.."
        git add .
        git commit -m "Auto commit - $(date)"
        git push
    else
        echo "Warning detected, skipping commit."
    fi
else
    echo "Required files missing"
fi

    