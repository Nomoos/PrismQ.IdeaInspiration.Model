@echo off
REM PrismQ.IdeaInspiration.Model Submodule Converter Script for Windows
REM Purpose: Adds related PrismQ modules as git submodules in the correct directory structure
REM Target: Windows with NVIDIA RTX 5090, AMD Ryzen, 64GB RAM

echo =====================================
echo PrismQ Submodule Converter
echo =====================================
echo.

REM Define the correct base path for submodules
REM Correct structure: PrismQ\mod\IdeaInspiration\mod\{ModuleName}
set BASE_PATH=PrismQ\mod\IdeaInspiration\mod

echo Creating directory structure: %BASE_PATH%
echo.

REM Create the base directory structure if it doesn't exist
if not exist "PrismQ\mod\IdeaInspiration\mod" (
    mkdir "PrismQ\mod\IdeaInspiration\mod"
    echo Created base directory structure.
) else (
    echo Base directory structure already exists.
)
echo.

REM Define the PrismQ modules to be added as submodules
REM Format: ModuleName|RepositoryURL
REM Note: Only include repositories that exist and are publicly accessible

set MODULES[0]=Classification|https://github.com/Nomoos/PrismQ.IdeaInspiration.Classification.git
set MODULES[1]=Scoring|https://github.com/Nomoos/PrismQ.IdeaInspiration.Scoring.git
set MODULES[2]=Builder|https://github.com/Nomoos/PrismQ.IdeaInspiration.Builder.git
REM set MODULES[3]=Sources|https://github.com/Nomoos/PrismQ.IdeaInspiration.Sources.git (Not yet available)

echo =====================================
echo Adding Submodules
echo =====================================
echo.

REM Add Classification submodule
echo Adding Classification module...
set MODULE_NAME=Classification
set MODULE_URL=https://github.com/Nomoos/PrismQ.IdeaInspiration.Classification.git
set MODULE_PATH=%BASE_PATH%\Classification

if exist "%MODULE_PATH%" (
    echo [SKIP] Classification already exists at %MODULE_PATH%
) else (
    git submodule add %MODULE_URL% %MODULE_PATH%
    if errorlevel 1 (
        echo [ERROR] Failed to add Classification submodule
    ) else (
        echo [OK] Classification added successfully to %MODULE_PATH%
    )
)
echo.

REM Add Scoring submodule
echo Adding Scoring module...
set MODULE_NAME=Scoring
set MODULE_URL=https://github.com/Nomoos/PrismQ.IdeaInspiration.Scoring.git
set MODULE_PATH=%BASE_PATH%\Scoring

if exist "%MODULE_PATH%" (
    echo [SKIP] Scoring already exists at %MODULE_PATH%
) else (
    git submodule add %MODULE_URL% %MODULE_PATH%
    if errorlevel 1 (
        echo [ERROR] Failed to add Scoring submodule
    ) else (
        echo [OK] Scoring added successfully to %MODULE_PATH%
    )
)
echo.

REM Add Builder submodule
echo Adding Builder module...
set MODULE_NAME=Builder
set MODULE_URL=https://github.com/Nomoos/PrismQ.IdeaInspiration.Builder.git
set MODULE_PATH=%BASE_PATH%\Builder

if exist "%MODULE_PATH%" (
    echo [SKIP] Builder already exists at %MODULE_PATH%
) else (
    git submodule add %MODULE_URL% %MODULE_PATH%
    if errorlevel 1 (
        echo [ERROR] Failed to add Builder submodule
    ) else (
        echo [OK] Builder added successfully to %MODULE_PATH%
    )
)
echo.

REM Add Sources submodule
echo Adding Sources module...
set MODULE_NAME=Sources
set MODULE_URL=https://github.com/Nomoos/PrismQ.IdeaInspiration.Sources.git
set MODULE_PATH=%BASE_PATH%\Sources

echo [INFO] Sources module repository not yet available - skipping for now
echo [INFO] To add Sources later, uncomment the Sources section in this script
REM Uncomment the following lines when Sources repository is available:
REM if exist "%MODULE_PATH%" (
REM     echo [SKIP] Sources already exists at %MODULE_PATH%
REM ) else (
REM     git submodule add %MODULE_URL% %MODULE_PATH%
REM     if errorlevel 1 (
REM         echo [ERROR] Failed to add Sources submodule
REM     ) else (
REM         echo [OK] Sources added successfully to %MODULE_PATH%
REM     )
REM )
echo.

echo =====================================
echo Initializing and Updating Submodules
echo =====================================
echo.

git submodule init
git submodule update

echo.
echo =====================================
echo Submodule Conversion Complete!
echo =====================================
echo.
echo All PrismQ modules have been added as submodules to:
echo   %BASE_PATH%\
echo.
echo Submodules added:
echo   - Classification (%BASE_PATH%\Classification)
echo   - Scoring        (%BASE_PATH%\Scoring)
echo   - Builder        (%BASE_PATH%\Builder)
REM echo   - Sources        (%BASE_PATH%\Sources) [Not yet available]
echo.
echo To update all submodules in the future, run:
echo   git submodule update --remote --merge
echo.

pause
