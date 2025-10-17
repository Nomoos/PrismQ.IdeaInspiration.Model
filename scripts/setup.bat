@echo off
REM PrismQ.IdeaInspiration.Model Setup Script for Windows
REM Target: Windows with NVIDIA RTX 5090, AMD Ryzen, 64GB RAM

echo =====================================
echo PrismQ.IdeaInspiration.Model Setup
echo =====================================
echo.

REM Navigate to repository root (parent of scripts directory)
cd /d "%~dp0.."

REM Set default Python executable
set PYTHON_EXEC=python

REM Read PYTHON_EXECUTABLE from .env if it exists
if exist ".env" (
    for /f "tokens=1,2 delims==" %%a in ('findstr /i "^PYTHON_EXECUTABLE=" .env') do (
        set PYTHON_EXEC=%%b
    )
)

REM Check Python installation
%PYTHON_EXEC% --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python executable '%PYTHON_EXEC%' is not found or not working
    echo Please install Python 3.8 or higher or update PYTHON_EXECUTABLE in .env
    exit /b 1
)

echo Python found: %PYTHON_EXEC%
echo.

REM Create virtual environment
echo Creating virtual environment...
if not exist "venv" (
    %PYTHON_EXEC% -m venv venv
    echo Virtual environment created.
) else (
    echo Virtual environment already exists.
)
echo.

REM Activate virtual environment and install dependencies
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing dependencies...
python -m pip install --upgrade pip
pip install -e ".[dev]"

echo.
echo =====================================
echo Setup Complete!
echo =====================================
echo.
echo To activate the virtual environment, run:
echo   venv\Scripts\activate.bat
echo.
echo To run tests:
echo   pytest
echo.

pause
