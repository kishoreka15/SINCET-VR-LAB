#!/bin/bash

# Run Flask app in the background
python3 app.py &

# Wait a bit to ensure Flask starts
sleep 3

# Start Serveo tunnel
ssh -R mylab:80:127.0.0.1:5000 serveo.net