@echo off
chcp 65001 >nul
title Install dependencies

cd /d "%~dp0"

echo Installing Python dependencies...

python --version
if %errorlevel% neq 0 (
    echo Python not found. Install Python from python.org and enable Add to PATH.
    pause
    exit /b
)

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo Done.
pause