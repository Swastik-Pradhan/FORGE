from pathlib import Path


def read_file(path: str, encoding: str = "utf-8") -> str:
    """
    Read and return the contents of a text file.
    """
    return Path(path).read_text(encoding=encoding)


def write_file(path: str, content: str, encoding: str = "utf-8") -> None:
    """
    Write content to a text file.
    """
    Path(path).write_text(content, encoding=encoding)


def exists(path: str) -> bool:
    """
    Check whether a file or directory exists.
    """
    return Path(path).exists()


def is_file(path: str) -> bool:
    """
    Check whether the path points to a file.
    """
    return Path(path).is_file()


def is_directory(path: str) -> bool:
    """
    Check whether the path points to a directory.
    """
    return Path(path).is_dir()


def filename(path: str) -> str:
    """
    Return the filename.
    """
    return Path(path).name


def extension(path: str) -> str:
    """
    Return the file extension.
    """
    return Path(path).suffix


def parent(path: str) -> Path:
    """
    Return the parent directory.
    """
    return Path(path).parent


def list_files(directory: str):
    """
    Return all files in a directory.
    """
    return [f for f in Path(directory).iterdir() if f.is_file()]