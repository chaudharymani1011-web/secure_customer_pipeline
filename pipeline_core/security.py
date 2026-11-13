import hashlib
from pathlib import Path

def safe_path(base, filename):
    base = Path(base).resolve()
    path = (base / filename).resolve()

    if not path.is_relative_to(base):
        raise ValueError("Unsafe file path")

    return path

def calculate_hash(file_path):
    sha = hashlib.sha256()

    with open(file_path, "rb") as file:
        sha.update(file.read())

    return sha.hexdigest()