# Submodule Converter Scripts

## Purpose

The `submodule-converter` scripts help organize related PrismQ modules as git submodules in the correct directory structure. These scripts add the following PrismQ ecosystem modules as git submodules:

- **PrismQ.IdeaInspiration.Classification** - Content classification system
- **PrismQ.IdeaInspiration.Scoring** - Content scoring engine  
- **PrismQ.IdeaInspiration.Builder** - Model construction from sources

## Directory Structure

The scripts create the following directory structure:

```
PrismQ/
└── mod/
    └── IdeaInspiration/
        └── mod/
            ├── Classification/
            ├── Scoring/
            └── Builder/
```

This structure ensures that:
1. All PrismQ modules are organized under the `PrismQ/` top-level directory
2. The `mod/` directory contains business/domain modules
3. Each module family (IdeaInspiration, etc.) has its own subdirectory
4. Related modules are grouped under the `mod/` subdirectory within their family

## Usage

### Windows

```batch
cd /path/to/PrismQ.IdeaInspiration.Model
scripts\submodule-converter.bat
```

### Linux/Unix/Mac

```bash
cd /path/to/PrismQ.IdeaInspiration.Model
bash scripts/submodule-converter.sh
```

## What the Scripts Do

1. **Create Directory Structure** - Creates the `PrismQ/mod/IdeaInspiration/mod/` directory hierarchy
2. **Add Submodules** - Adds each PrismQ module as a git submodule in the correct location
3. **Initialize Submodules** - Runs `git submodule init` and `git submodule update`
4. **Skip Existing** - Checks if submodules already exist to avoid conflicts

## After Running the Script

After the script completes:

1. The `.gitmodules` file will be created/updated with submodule references
2. The submodule directories will be created and populated
3. You can work with the submodules as needed

## Updating Submodules

To update all submodules to their latest versions:

```bash
git submodule update --remote --merge
```

## Requirements

- Git must be installed and available in PATH
- Network access to GitHub to clone the submodule repositories
- Write permissions in the current repository

## Troubleshooting

### Authentication Required

If you get authentication prompts, ensure you have:
- SSH keys configured for GitHub, OR
- A GitHub personal access token configured

### Repository Not Found

Some repositories may not be publicly available yet. The script will skip these with an informational message.

### Submodule Already Exists

If a submodule already exists, the script will skip it and display a `[SKIP]` message.

## Notes

- The **Sources** module repository is not yet available and will be skipped automatically
- When the Sources repository becomes available, uncomment the relevant section in the script
- The scripts are idempotent - you can run them multiple times safely
