#!/bin/bash

# Check and kill conflicting processes on port 5000
echo "Checking for processes on port 5000..."
PID=$(lsof -t -i:5000)

if [ -n "$PID" ]; then
    echo "Process with PID $PID found on port 5000. Killing it..."
    kill -9 "$PID"
    echo "Process killed."
else
    echo "No conflicting processes found on port 5000."
fi

# Activate the virtual environment
echo "Activating virtual environment..."
. myenv/bin/activate

# Run the Flask application
echo "Starting Flask application..."
python -m flask run
