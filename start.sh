#!/bin/bash
echo "Starting application..."
# Ensure time synchronization
current_time=$(curl -s --head http://worldtimeapi.org/api/timezone/Etc/UTC | grep ^Date: | sed 's/Date: //g')
date -u -s "$current_time"
sleep 5  # Wait for time sync
echo "Time synchronized: $(date)"
# Start the application
python SiestaRobot/__main__.py