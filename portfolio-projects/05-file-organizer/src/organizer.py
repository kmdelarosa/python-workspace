"""File move logic and conflict resolution."""
import logging
import shutil
from pathlib import Path
from datetime import datetime

logging.basicConfig(
    filename="logs/organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)


def organize(target: str, config: dict, dry_run: bool = False):
    target_path = Path(target)
    if not target_path.is_dir():
        print(f"Error: '{target}' is not a valid directory.")
        return

    for file in target_path.iterdir():
        if not file.is_file():
            continue

        ext = file.suffix.lower()
        folder_name = config.get(ext, "Other")
        date_subfolder = datetime.now().strftime("%Y-%m")
        dest_dir = target_path / folder_name / date_subfolder
        dest = dest_dir / file.name

        # Resolve conflicts
        if dest.exists():
            dest = _resolve_conflict(dest)

        if dry_run:
            print(f"[DRY RUN] {file.name} → {dest.relative_to(target_path)}")
        else:
            dest_dir.mkdir(parents=True, exist_ok=True)
            shutil.move(str(file), str(dest))
            logging.info(f"Moved: {file} → {dest}")
            print(f"Moved: {file.name} → {dest.relative_to(target_path)}")


def _resolve_conflict(dest: Path) -> Path:
    counter = 1
    stem = dest.stem
    suffix = dest.suffix
    parent = dest.parent
    while dest.exists():
        dest = parent / f"{stem}_{counter}{suffix}"
        counter += 1
    return dest
