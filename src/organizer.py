from pathlib import Path
import shutil

from src.config import FILE_TYPES, DEFAULT_CATEGORY


def get_category(extension: str) -> str:
    """Return the category for a file extension."""

    for category, extensions in FILE_TYPES.items():

        if extension in extensions:
            return category

    return DEFAULT_CATEGORY


def create_category_folder(base_path: Path, category: str) -> Path:
    """Create and return the category folder."""

    destination = base_path / category

    destination.mkdir(
        parents=True,
        exist_ok=True
    )

    return destination


def move_file(file: Path, destination: Path) -> None:
    """Move a file to the destination folder."""

    target = destination / file.name

    shutil.move(
        str(file),
        str(target)
    )


def organize_folder(folder_path: Path) -> None:
    """Organize all files inside a folder."""

    for file in folder_path.iterdir():

        # Ignore directories
        if not file.is_file():
            continue

        extension = file.suffix.lower()

        category = get_category(extension)

        destination = create_category_folder(
            folder_path,
            category
        )

        move_file(
            file,
            destination
        )

        print(
            f"Moved: {file.name} → {category}/"
        )