@echo off
:: START_CONVERTER.bat
:: Batch script to check for Python and PyYAML, then run the home file converter.

echo.
echo === Home Converter Launcher ===
echo.

:: Check if Python is available
echo Checking for Python installation...
py --version >nul 2>&1
if errorlevel 1 (
    echo [!] Python is not installed or not in your system PATH.
    echo Please install Python from https://www.python.org/downloads/
    echo Be sure to check "Add Python to PATH" during installation.
    pause
    exit /b
)

:: Check if PyYAML is installed
echo Checking for PyYAML...
pip show pyyaml >nul 2>&1
if errorlevel 1 (
    echo PyYAML not found. Installing...
    py -m pip install pyyaml
)

echo.
echo Starting converter...
echo --------------------------
py homes_converter.py

echo.
pause
