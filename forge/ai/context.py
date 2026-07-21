from pathlib import Path

from forge.utils.files import read_file
from forge.utils.json_utils import read_json
from forge.ai.codemap import build_code_map
from forge.ai.constants import IGNORE_DIRECTORIES


# ==========================================================
# Important project files (higher number = higher priority)
# ==========================================================

IMPORTANT_FILENAMES = {
    # Documentation
    "README.md": 100,
    "README.txt": 95,
    "README.rst": 95,

    # Python
    "pyproject.toml": 95,
    "requirements.txt": 90,

    # JavaScript / TypeScript
    "package.json": 95,

    # Rust
    "Cargo.toml": 95,

    # Go
    "go.mod": 95,

    # Java
    "pom.xml": 95,
    "build.gradle": 95,

    # Containers
    "Dockerfile": 80,

    # Environment
    ".env.example": 70,

    # Ignore rules
    ".gitignore": 40,
}


# ==========================================================
# Common project entry points
# ==========================================================

ENTRY_POINT_NAMES = {
    "main.py": 90,
    "app.py": 90,
    "manage.py": 90,

    "main.go": 90,

    "main.rs": 90,

    "index.js": 90,
    "server.js": 90,

    "main.ts": 90,
    "server.ts": 90,

    "Main.java": 90,
}


# ==========================================================
# Ignore directories
# ==========================================================

IGNORE_DIRECTORIES = {
    ".git",
    ".forge",
    "__pycache__",
    "venv",
    ".venv",
    "node_modules",
    "dist",
    "build",
    ".idea",
    ".vscode",
}


# ==========================================================
# Context limits
# ==========================================================

MAX_CONTEXT_SIZE = 15000
MAX_FILE_SIZE = 3000


def build_directory_tree(root: Path, max_depth: int = 2) -> str:
    """
    Build a simple directory tree.
    """

    lines = []

    def walk(directory: Path, prefix: str = "", depth: int = 0):

        if depth > max_depth:
            return

        try:
            children = sorted(
                directory.iterdir(),
                key=lambda p: (p.is_file(), p.name.lower())
            )
        except PermissionError:
            return

        for child in children:

            if child.name.startswith("."):
                continue

            if child.name in IGNORE_DIRECTORIES:
                continue

            lines.append(f"{prefix}{child.name}")

            if child.is_dir():
                walk(
                    child,
                    prefix + "    ",
                    depth + 1
                )

    walk(root)

    return "\n".join(lines)


def discover_important_files(root: Path) -> list[Path]:
    """
    Discover and rank important project files.
    """

    discovered: list[tuple[int, Path]] = []

    for path in root.rglob("*"):

        if not path.is_file():
            continue

        if any(part in IGNORE_DIRECTORIES for part in path.parts):
            continue

        priority = None

        if path.name in IMPORTANT_FILENAMES:
            priority = IMPORTANT_FILENAMES[path.name]

        elif path.name in ENTRY_POINT_NAMES:
            priority = ENTRY_POINT_NAMES[path.name]

        if priority is not None:
            discovered.append((priority, path))

    # Highest priority first
    discovered.sort(
        key=lambda item: (-item[0], str(item[1]))
    )

    return [path for _, path in discovered]


def build_project_context(project_root: str = ".") -> str:
    """
    Build a textual context describing the project.
    """

    root = Path(project_root).resolve()

    context: list[str] = []
    current_size = 0

    # ==========================================================
    # Project Metadata
    # ==========================================================

    index_path = root / ".forge" / "index.json"

    if index_path.exists():

        index = read_json(index_path)

        metadata = (
            "===== PROJECT METADATA =====\n\n"
            f"{index}"
        )

        context.append(metadata)
        current_size += len(metadata)

    # ==========================================================
    # Directory Structure
    # ==========================================================

    tree = (
        "===== DIRECTORY STRUCTURE =====\n\n"
        f"{build_directory_tree(root)}"
    )

    if current_size < MAX_CONTEXT_SIZE:
        context.append(tree)
        current_size += len(tree)

    # ==========================================================
    # Code Map
    # ==========================================================

    remaining = MAX_CONTEXT_SIZE - current_size

    if remaining > 0:

        code_map = (
            "===== CODE MAP =====\n\n"
            f"{build_code_map(root)}"
        )

        # Don't let the code map consume the entire context
        code_map = code_map[:min(5000, remaining)]

        context.append(code_map)
        current_size += len(code_map)

    # ==========================================================
    # Important Files
    # ==========================================================

    for file_path in discover_important_files(root):

        if current_size >= MAX_CONTEXT_SIZE:
            break

        try:

            content = read_file(str(file_path))

        except Exception:

            content = "(Unable to read file)"

        remaining = MAX_CONTEXT_SIZE - current_size

        if remaining <= 0:
            break

        content = content[: min(MAX_FILE_SIZE, remaining)]

        section = (
            f"===== {file_path.relative_to(root)} =====\n\n"
            f"{content}"
        )

        context.append(section)
        current_size += len(section)

    return "\n\n".join(context)