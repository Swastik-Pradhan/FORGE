from forge.ai.constants import (
    IGNORE_DIRECTORIES,
    SUPPORTED_EXTENSIONS,
)
from forge.ai.models import ProjectScanResult
from forge.utils.validators import validate_directory


def scan_project(path: str = ".") -> ProjectScanResult:
    """
    Scan a project directory and collect metadata.
    """

    root_path = validate_directory(path).resolve()

    total_files = 0
    total_directories = 0
    total_size = 0

    largest_file = ""
    largest_file_size = 0

    file_types: dict[str, int] = {}
    files: list[str] = []

    for entry in root_path.rglob("*"):

        # Skip ignored directories
        if any(part in IGNORE_DIRECTORIES for part in entry.parts):
            continue

        # Count directories
        if entry.is_dir():
            total_directories += 1
            continue

        # Ignore unsupported file types
        if entry.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue

        total_files += 1

        size = entry.stat().st_size
        total_size += size

        relative_path = str(entry.relative_to(root_path))
        files.append(relative_path)

        # Count file extensions
        extension = entry.suffix.lower()
        file_types[extension] = file_types.get(extension, 0) + 1

        # Track largest file
        if size > largest_file_size:
            largest_file_size = size
            largest_file = relative_path

    return ProjectScanResult(
        project_name=root_path.name,
        root_path=str(root_path),
        total_files=total_files,
        total_directories=total_directories,
        total_size=total_size,
        largest_file=largest_file,
        largest_file_size=largest_file_size,
        file_types=file_types,
        files=files,
    )