#!/bin/bash

echo "=============================="
echo " Server Monitor - $(date)"
echo "=============================="
echo ""

echo "Running server health check..."
python3 ~/IdeaProjects/devops_journey/day3.py

echo ""
echo "=============================="
echo "Auto committing to GitHub..."
cd ~/IdeaProjects/devops_journey
git add .
git commit -m "Auto commit - $(date)"
git push

echo ""
echo "=============================="
echo "Done!"