from pathlib import Path
import argparse

from src.organizer import organize_folder


VERSION = "1.0.0"


def create_parser():
    parser = argparse.ArgumentParser(
        prog="fileflow",
        description="FileFlow - A simple file organization tool."
    )

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"FileFlow {VERSION}",
        help="Show FileFlow version"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    # PATH command
    path_parser = subparsers.add_parser(
        "path",
        help="Organize files in a specified folder"
    )

    path_parser.add_argument(
        "folder",
        help="Path of the folder to organize"
    )

    return parser


def handle_path_command(folder):
    folder_path = Path(folder).expanduser()

    if not folder_path.exists():
        print(f"Error: folder does not exist: {folder_path}")
        return

    if not folder_path.is_dir():
        print(f"Error: not a folder: {folder_path}")
        return

    organize_folder(folder_path)


def main():
    parser = create_parser()

    args = parser.parse_args()

    if args.command == "path":
        handle_path_command(args.folder)


if __name__ == "__main__":
    main()