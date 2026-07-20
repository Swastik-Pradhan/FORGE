import hashlib
from pathlib import Path


def sha256(file_path: str) -> str:
    """
    Compute SHA-256 hash of a file.
    """

    h = hashlib.sha256()

    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)

    return h.hexdigest()


def md5(file_path: str) -> str:
    """
    Compute MD5 hash.
    """

    h = hashlib.md5()

    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)

    return h.hexdigest()


def sha1(file_path: str) -> str:
    """
    Compute SHA-1 hash.
    """

    h = hashlib.sha1()

    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)

    return h.hexdigest()