#!/bin/bash
echo "Starting application..."
# Ensure time synchronization
ntpdate ntp.ubuntu.com
sleep 5  # Wait for time sync
echo "Time synchronized: $(date)"
# Start the application
python SiestaRobot/__main__.py