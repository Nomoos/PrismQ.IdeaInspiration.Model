@echo off
REM PrismQ.IdeaInspiration.Model - Database Setup Script
REM This script creates db.s3db in the user's working directory and sets up the IdeaInspiration table
REM Target: Windows with NVIDIA RTX 5090, AMD Ryzen, 64GB RAM

setlocal enabledelayedexpansion

echo ============================================================
echo PrismQ.IdeaInspiration.Model - Database Setup
echo ============================================================
echo.

REM Store the repository root (where this script is located)
set "SCRIPT_DIR=%~dp0"
cd /d "%SCRIPT_DIR%"

REM Set default Python executable
set "PYTHON_EXEC=python"

REM Check if .env file exists, if not, create from example
if not exist ".env" (
    echo [INFO] .env file not found.
    if exist ".env.example" (
        echo [INFO] Creating .env from .env.example...
        copy ".env.example" ".env" >nul
        echo [INFO] .env file created.
    ) else (
        echo [INFO] Creating new .env file...
        (
            echo # PrismQ Module Configuration
            echo APP_NAME=PrismQ.IdeaInspiration.Model
            echo APP_ENV=development
            echo DEBUG=true
            echo LOG_LEVEL=INFO
            echo PYTHON_EXECUTABLE=python
        ) > ".env"
        echo [INFO] .env file created with default values.
    )
    echo.
)

REM Read PYTHON_EXECUTABLE from .env if it exists
for /f "tokens=1,2 delims==" %%a in ('findstr /i "^PYTHON_EXECUTABLE=" .env 2^>nul') do (
    set "PYTHON_EXEC=%%b"
)

REM Remove any leading/trailing spaces
set "PYTHON_EXEC=%PYTHON_EXEC: =%"

REM Check if Python executable exists
%PYTHON_EXEC% --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo [ERROR] Python executable '%PYTHON_EXEC%' not found or not working.
    echo.
    set /p "PYTHON_INPUT=Please enter the Python executable path (e.g., python, python3, C:\Python310\python.exe): "
    
    REM Update the user's input
    set "PYTHON_EXEC=!PYTHON_INPUT!"
    
    REM Test again
    !PYTHON_EXEC! --version >nul 2>&1
    if errorlevel 1 (
        echo [ERROR] Python executable '!PYTHON_EXEC!' still not working.
        echo [ERROR] Please install Python 3.8 or higher and try again.
        pause
        exit /b 1
    )
    
    REM Update .env with the working Python executable
    echo [INFO] Updating .env with Python executable: !PYTHON_EXEC!
    powershell -Command "(Get-Content .env) -replace '^PYTHON_EXECUTABLE=.*', 'PYTHON_EXECUTABLE=!PYTHON_EXEC!' | Set-Content .env"
)

echo [INFO] Using Python: %PYTHON_EXEC%
%PYTHON_EXEC% --version
echo.

REM Get the current working directory (where user called the script from)
set "USER_WORK_DIR=%CD%"
echo [INFO] Current working directory: %USER_WORK_DIR%
echo.

REM Ask user where to create the database
echo The database will be created in your current working directory.
set /p "CONFIRM=Create db.s3db in '%USER_WORK_DIR%'? (Y/N): "

if /i not "%CONFIRM%"=="Y" (
    echo.
    set /p "CUSTOM_DIR=Enter the full path where you want to create db.s3db: "
    set "USER_WORK_DIR=!CUSTOM_DIR!"
)

REM Create the database path
set "DB_PATH=%USER_WORK_DIR%\db.s3db"
echo.
echo [INFO] Database will be created at: %DB_PATH%
echo.

REM Create Python script to set up the database
echo [INFO] Creating database and IdeaInspiration table...
%PYTHON_EXEC% -c "import sqlite3; import sys; db_path = r'%DB_PATH%'; conn = sqlite3.connect(db_path); cursor = conn.cursor(); cursor.execute('''CREATE TABLE IF NOT EXISTS IdeaInspiration (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, description TEXT, content TEXT, keywords TEXT, source_type TEXT, metadata TEXT, source_id TEXT, source_url TEXT, score INTEGER, category TEXT, subcategory_relevance TEXT, contextual_category_scores TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)'''); conn.commit(); conn.close(); print('[SUCCESS] Database and IdeaInspiration table created successfully!')"

if errorlevel 1 (
    echo.
    echo [ERROR] Failed to create database or table.
    pause
    exit /b 1
)

echo.
echo ============================================================
echo Setup Complete!
echo ============================================================
echo.
echo Database Location: %DB_PATH%
echo Table Created: IdeaInspiration
echo.
echo Table Schema:
echo   - id: INTEGER PRIMARY KEY AUTOINCREMENT
echo   - title: TEXT NOT NULL
echo   - description: TEXT
echo   - content: TEXT
echo   - keywords: TEXT (JSON array)
echo   - source_type: TEXT (text/video/audio/unknown)
echo   - metadata: TEXT (JSON object with string key-value pairs)
echo   - source_id: TEXT
echo   - source_url: TEXT
echo   - score: INTEGER
echo   - category: TEXT
echo   - subcategory_relevance: TEXT (JSON object with int values)
echo   - contextual_category_scores: TEXT (JSON object with int values)
echo   - created_at: TIMESTAMP
echo   - updated_at: TIMESTAMP
echo.
echo You can now use this database with PrismQ modules.
echo.
pause
