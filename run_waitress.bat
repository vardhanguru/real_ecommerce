@echo off
REM Waitress server runner for Django application (Windows Batch)
REM Run this batch file to start the application with Waitress WSGI server

setlocal enabledelayedexpansion

REM Set default values
if not defined HOST set HOST=0.0.0.0
if not defined PORT set PORT=8000

echo.
echo ============================================================
echo Starting Waitress server at http://%HOST%:%PORT%
echo ============================================================
echo.

REM Run the Python script
python run_waitress.py

pause
