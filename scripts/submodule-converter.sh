#!/bin/bash
# PrismQ.IdeaInspiration.Model Submodule Converter Script for Linux/Unix
# Purpose: Adds related PrismQ modules as git submodules in the correct directory structure
# Target: Linux/Unix systems

echo "====================================="
echo "PrismQ Submodule Converter"
echo "====================================="
echo ""

# Define the correct base path for submodules
# Correct structure: PrismQ/mod/IdeaInspiration/mod/{ModuleName}
BASE_PATH="PrismQ/mod/IdeaInspiration/mod"

echo "Creating directory structure: $BASE_PATH"
echo ""

# Create the base directory structure if it doesn't exist
if [ ! -d "PrismQ/mod/IdeaInspiration/mod" ]; then
    mkdir -p "PrismQ/mod/IdeaInspiration/mod"
    echo "Created base directory structure."
else
    echo "Base directory structure already exists."
fi
echo ""

echo "====================================="
echo "Adding Submodules"
echo "====================================="
echo ""

# Add Classification submodule
echo "Adding Classification module..."
MODULE_NAME="Classification"
MODULE_URL="https://github.com/Nomoos/PrismQ.IdeaInspiration.Classification.git"
MODULE_PATH="$BASE_PATH/Classification"

if [ -d "$MODULE_PATH" ]; then
    echo "[SKIP] Classification already exists at $MODULE_PATH"
else
    git submodule add "$MODULE_URL" "$MODULE_PATH"
    if [ $? -eq 0 ]; then
        echo "[OK] Classification added successfully to $MODULE_PATH"
    else
        echo "[ERROR] Failed to add Classification submodule"
    fi
fi
echo ""

# Add Scoring submodule
echo "Adding Scoring module..."
MODULE_NAME="Scoring"
MODULE_URL="https://github.com/Nomoos/PrismQ.IdeaInspiration.Scoring.git"
MODULE_PATH="$BASE_PATH/Scoring"

if [ -d "$MODULE_PATH" ]; then
    echo "[SKIP] Scoring already exists at $MODULE_PATH"
else
    git submodule add "$MODULE_URL" "$MODULE_PATH"
    if [ $? -eq 0 ]; then
        echo "[OK] Scoring added successfully to $MODULE_PATH"
    else
        echo "[ERROR] Failed to add Scoring submodule"
    fi
fi
echo ""

# Add Builder submodule
echo "Adding Builder module..."
MODULE_NAME="Builder"
MODULE_URL="https://github.com/Nomoos/PrismQ.IdeaInspiration.Builder.git"
MODULE_PATH="$BASE_PATH/Builder"

if [ -d "$MODULE_PATH" ]; then
    echo "[SKIP] Builder already exists at $MODULE_PATH"
else
    git submodule add "$MODULE_URL" "$MODULE_PATH"
    if [ $? -eq 0 ]; then
        echo "[OK] Builder added successfully to $MODULE_PATH"
    else
        echo "[ERROR] Failed to add Builder submodule"
    fi
fi
echo ""

# Add Sources submodule
echo "Adding Sources module..."
MODULE_NAME="Sources"
MODULE_URL="https://github.com/Nomoos/PrismQ.IdeaInspiration.Sources.git"
MODULE_PATH="$BASE_PATH/Sources"

echo "[INFO] Sources module repository not yet available - skipping for now"
echo "[INFO] To add Sources later, uncomment the Sources section in this script"
# Uncomment the following lines when Sources repository is available:
# if [ -d "$MODULE_PATH" ]; then
#     echo "[SKIP] Sources already exists at $MODULE_PATH"
# else
#     git submodule add "$MODULE_URL" "$MODULE_PATH"
#     if [ $? -eq 0 ]; then
#         echo "[OK] Sources added successfully to $MODULE_PATH"
#     else
#         echo "[ERROR] Failed to add Sources submodule"
#     fi
# fi
echo ""

echo "====================================="
echo "Initializing and Updating Submodules"
echo "====================================="
echo ""

git submodule init
git submodule update

echo ""
echo "====================================="
echo "Submodule Conversion Complete!"
echo "====================================="
echo ""
echo "All PrismQ modules have been added as submodules to:"
echo "  $BASE_PATH/"
echo ""
echo "Submodules added:"
echo "  - Classification ($BASE_PATH/Classification)"
echo "  - Scoring        ($BASE_PATH/Scoring)"
echo "  - Builder        ($BASE_PATH/Builder)"
# echo "  - Sources        ($BASE_PATH/Sources) [Not yet available]"
echo ""
echo "To update all submodules in the future, run:"
echo "  git submodule update --remote --merge"
echo ""
