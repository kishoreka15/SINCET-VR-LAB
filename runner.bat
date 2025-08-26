@echo off
REM Run Flask app
start cmd /k python app.py

REM Wait a bit to ensure Flask starts (optional)
timeout /t 3

REM Start Serveo tunnel
start cmd /k ssh -R mylab:80:127.0.0.1:5000 serveo.net