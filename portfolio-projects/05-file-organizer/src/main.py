"""Entry point for the File Organizer."""
import argparse
from organizer import organize
from config import load_config


def main():
    parser = argparse.ArgumentParser(description="Automated File Organizer")
    parser.add_argument("--target", required=True, help="Folder to organize")
    parser.add_argument("--dry-run", action="store_true", help="Preview without moving files")
    args = parser.parse_args()

    config = load_config()
    organize(args.target, config, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
