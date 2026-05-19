# Waitress server runner for Django application (PowerShell)
# Run this script to start the application with Waitress WSGI server
# Usage: .\run_waitress.ps1 -Host "0.0.0.0" -Port 8000

param(
    [string]$Host = "0.0.0.0",
    [int]$Port = 8000
)

Write-Host ""
Write-Host "============================================================"
Write-Host "Starting Waitress server at http://$Host`:$Port"
Write-Host "============================================================"
Write-Host ""

# Set environment variables
$env:HOST = $Host
$env:PORT = $Port

# Run the Python script
python run_waitress.py

# Keep window open on error
if ($LASTEXITCODE -ne 0) {
    Write-Host "Press any key to close..."
    Read-Host
}
