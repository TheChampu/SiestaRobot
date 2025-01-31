#!/bin/bash
#!/bin/bash
echo "Starting application..."
# Ensure time synchronization
sudo timedatectl set-ntp on
sleep 5  # Wait for time sync
echo "Time synchronized: $(date)"
# Start the application
python __main__.py
chmod +x start.sh