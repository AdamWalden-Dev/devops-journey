#!/bin/bash

NAME="Adam"
echo "Welcome, $NAME"
echo "Today's date is $(date)"
HOUR=$(date +%H)
if [ $HOUR -lt 12 ]; then
    echo "Good Morning!"
elif [ $HOUR -lt 17 ]; then
    echo "Good Afternoon!"
else
    echo "Good Evening!"
fi
python3 ~/IdeaProjects/devops_journey/day3.python
git add .
git commit -m "$(date) Testing Bash scripting/commands)"
git push
echo "All Done!"