@echo off
REM PrismQ.IdeaInspiration.Model Quick Start Script for Windows
REM Target: Windows with NVIDIA RTX 5090, AMD Ryzen, 64GB RAM

echo =====================================
echo PrismQ.IdeaInspiration.Model Quick Start
echo =====================================
echo.

REM Navigate to repository root (parent of scripts directory)
cd /d "%~dp0.."

REM Check if virtual environment exists
if not exist "venv" (
    echo Virtual environment not found!
    echo Please run setup.bat first.
    pause
    exit /b 1
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Check if .env exists
if not exist ".env" (
    echo WARNING: .env file not found!
    echo Copying .env.example to .env...
    copy .env.example .env
    echo.
    echo Please edit .env with your configuration before running.
    pause
)

echo.
echo Running example script...
echo Target: Windows, NVIDIA RTX 5090, AMD Ryzen, 64GB RAM
echo.

REM Run the example
python example.py

echo.
echo =====================================
echo Quick Start Complete!
echo =====================================
echo.

pause
