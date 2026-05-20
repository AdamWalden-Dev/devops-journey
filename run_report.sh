#!/bin/bash

if [ ! $(command -v python3) ]; then
    echo "Python3 not installed"
    exit 1
fi


if [ ! -f "system_report.py" ]; then
    echo "Unexpected ERROR"
    exit 1
fi

python3 system_report.py

if [ $? -eq 0 ]; then
    echo "Success"
else
    echo "sys.exit FAILED. Check python code for errors"
fi