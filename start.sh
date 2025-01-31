#!/bin/bash
echo "Starting application..."
# Ensure time synchronization
sudo ntpdate ntp.ubuntu.com
sleep 5  # Wait for time sync
echo "Time synchronized: $(date)"
# Start the application
python __main__.py