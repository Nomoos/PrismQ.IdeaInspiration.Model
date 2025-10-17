#!/bin/bash
# PrismQ.IdeaInspiration.Model - Database Setup Script (Linux/macOS)
# This script creates db.s3db and sets up the IdeaInspiration table
# Target: Linux CI/testing environments (GitHub Actions, etc.)

set -e  # Exit on error

echo "============================================================"
echo "PrismQ.IdeaInspiration.Model - Database Setup (Linux)"
echo "============================================================"
echo ""

# Store the repository root (where this script is located)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Set default Python executable
PYTHON_EXEC="python3"

# Check if .env file exists, if not, create it
if [ ! -f ".env" ]; then
    echo "[INFO] .env file not found."
    echo "[INFO] Creating new .env file..."
    cat > .env << 'EOF'
# PrismQ Module Configuration
APP_NAME=PrismQ.IdeaInspiration.Model
APP_ENV=development
DEBUG=true
LOG_LEVEL=INFO
PYTHON_EXECUTABLE=python3
EOF
    echo "[INFO] .env file created with default values."
    echo ""
fi

# Read PYTHON_EXECUTABLE from .env if it exists
if [ -f ".env" ]; then
    while IFS='=' read -r key value; do
        if [[ $key == "PYTHON_EXECUTABLE" ]]; then
            # Remove leading/trailing whitespace
            PYTHON_EXEC=$(echo "$value" | xargs)
            break
        fi
    done < <(grep "^PYTHON_EXECUTABLE=" .env)
fi

# Check if Python executable exists
if ! command -v "$PYTHON_EXEC" &> /dev/null; then
    echo ""
    echo "[ERROR] Python executable '$PYTHON_EXEC' not found or not working."
    echo "[ERROR] Please install Python 3.8 or higher and try again."
    exit 1
fi

echo "[INFO] Using Python: $PYTHON_EXEC"
$PYTHON_EXEC --version
echo ""

# Get the current working directory
USER_WORK_DIR="$(pwd)"
echo "[INFO] Current working directory: $USER_WORK_DIR"
echo ""

# For non-interactive mode (CI), skip confirmation
if [ -t 0 ]; then
    # Interactive mode
    echo "The database will be created in your current working directory."
    read -p "Create db.s3db in '$USER_WORK_DIR'? (Y/N): " CONFIRM
    
    if [[ ! "$CONFIRM" =~ ^[Yy]$ ]]; then
        echo ""
        read -p "Enter the full path where you want to create db.s3db: " CUSTOM_DIR
        USER_WORK_DIR="$CUSTOM_DIR"
    fi
else
    # Non-interactive mode (CI)
    echo "[INFO] Non-interactive mode detected. Using current directory."
fi

# Create the database path
DB_PATH="$USER_WORK_DIR/db.s3db"
echo ""
echo "[INFO] Database will be created at: $DB_PATH"
echo ""

# Create database and table
echo "[INFO] Creating database and IdeaInspiration table..."
$PYTHON_EXEC -c "
import sqlite3
import sys

db_path = '$DB_PATH'

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS IdeaInspiration (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            content TEXT,
            keywords TEXT,
            source_type TEXT,
            metadata TEXT,
            source_id TEXT,
            source_url TEXT,
            score INTEGER,
            category TEXT,
            subcategory_relevance TEXT,
            contextual_category_scores TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()
    print('[SUCCESS] Database and IdeaInspiration table created successfully!')
except Exception as e:
    print(f'[ERROR] Failed to create database or table: {e}', file=sys.stderr)
    sys.exit(1)
"

if [ $? -ne 0 ]; then
    echo ""
    echo "[ERROR] Failed to create database or table."
    exit 1
fi

echo ""
echo "============================================================"
echo "Setup Complete!"
echo "============================================================"
echo ""
echo "Database Location: $DB_PATH"
echo "Table Created: IdeaInspiration"
echo ""
echo "Table Schema:"
echo "  - id: INTEGER PRIMARY KEY AUTOINCREMENT"
echo "  - title: TEXT NOT NULL"
echo "  - description: TEXT"
echo "  - content: TEXT"
echo "  - keywords: TEXT (JSON array)"
echo "  - source_type: TEXT (text/video/audio/unknown)"
echo "  - metadata: TEXT (JSON object with string key-value pairs)"
echo "  - source_id: TEXT"
echo "  - source_url: TEXT"
echo "  - score: INTEGER"
echo "  - category: TEXT"
echo "  - subcategory_relevance: TEXT (JSON object with int values)"
echo "  - contextual_category_scores: TEXT (JSON object with int values)"
echo "  - created_at: TIMESTAMP"
echo "  - updated_at: TIMESTAMP"
echo ""
echo "You can now use this database with PrismQ modules."
echo ""
