# Automated File Organizer

A script that sorts a target folder by file type and date into structured subfolders.

## Portfolio Description

An automated file organizer that sorts a target directory by file type and date into structured subfolders. Configurable extension-to-folder mappings, conflict resolution for duplicate filenames, and a dry-run preview mode. Uses Python's `pathlib` and `shutil` for file operations, with full logging of every action taken.

## Features

- Configurable extension-to-folder rules (e.g. `.pdf` → `Documents`)
- Sort into dated subfolders (e.g. `Images/2026-08/`)
- Dry-run mode: preview moves without executing
- Duplicate filename conflict resolution (auto-rename)
- Full operation log written to file
- Optional: live folder watching with `watchdog`

## Tech Stack

- Python 3
- `os`, `shutil`, `pathlib`, `logging`
- `watchdog` (optional)

## Project Structure

```
05-file-organizer/
├── README.md
├── requirements.txt
├── config.json             # extension → folder mapping rules
├── logs/                   # operation logs written here
├── src/
│   ├── __init__.py
│   ├── main.py             # entry point, CLI args
│   ├── organizer.py        # move logic, conflict resolution
│   ├── config.py           # load and validate config.json
│   └── watcher.py          # optional watchdog integration
└── tests/
    └── test_organizer.py
```

## Getting Started

```bash
pip install -r requirements.txt

# Dry run first
python src/main.py --target ~/Downloads --dry-run

# Run for real
python src/main.py --target ~/Downloads
```

## Configuration

Edit `config.json` to define your own extension mappings:

```json
{
  ".pdf": "Documents",
  ".jpg": "Images",
  ".png": "Images",
  ".mp4": "Videos",
  ".zip": "Archives"
}
```

## Status

🚧 In progress
