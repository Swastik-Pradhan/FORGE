from pathlib import Path


def validate_directory(path: str) -> Path:
    """
    Validate that a directory exists and return a Path object.
    """

    p = Path(path)

    if not p.exists():
        raise FileNotFoundError(f"Directory '{path}' does not exist.")

    if not p.is_dir():
        raise NotADirectoryError(f"'{path}' is not a directory.")

    return p