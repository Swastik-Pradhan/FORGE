from forge.dev.templates import (
    README_TEMPLATE,
    DOCKERFILE_TEMPLATE,
    GITIGNORE_TEMPLATE,
)

from forge.utils.files import write_file


def generate_readme(project_name: str):
    write_file(
        "README.md",
        README_TEMPLATE.format(project=project_name),
    )


def generate_dockerfile():
    write_file(
        "Dockerfile",
        DOCKERFILE_TEMPLATE,
    )


def generate_gitignore():
    write_file(
        ".gitignore",
        GITIGNORE_TEMPLATE,
    )