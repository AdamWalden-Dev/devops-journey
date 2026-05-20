#!/bin/bash

if [ ! $(command -v python3) ]; then
    echo "Python3 not installed"
    exit 1
fi


if [ ! -f "system_report.py" ]; then
    echo "ERROR: system_report.py not found. Ensure you are running this script from the same directory as system_report.py "
    exit 1
fi
echo "Running system report..."

python3 system_report.py

if [ $? -eq 0 ]; then
    echo "Report generated successfully. Check the logs/ folder for output."
else
    echo "sys.exit FAILED. Check python code for errors"
fi