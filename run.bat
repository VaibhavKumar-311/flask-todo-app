@echo off
cd /d "%~dp0"

if not exist "venv\Scripts\python.exe" (
    echo Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: python not found. Install Python 3.10+ and ensure it is on PATH.
        pause
        exit /b 1
    )
    echo Installing dependencies...
    call venv\Scripts\pip.exe install -r requirements.txt
    if errorlevel 1 (
        echo ERROR: pip install failed.
        pause
        exit /b 1
    )
)

echo Starting Flask at http://127.0.0.1:5000
echo Press Ctrl+C to stop.
venv\Scripts\python.exe app.py
