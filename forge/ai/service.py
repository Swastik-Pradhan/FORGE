import ollama

from forge.ai.context import build_project_context
from forge.ai.indexer import create_index
from forge.ai.models import ProjectScanResult, SummaryResult
from forge.ai.prompts import (
    SUMMARY_PROMPT,
    PROJECT_SUMMARY_PROMPT,
)
from forge.ai.scanner import scan_project

from forge.utils.config import DEFAULT_MODEL
from forge.utils.files import read_file


def summarize_file(file_path: str) -> SummaryResult:
    """
    Read a file and summarize it using Ollama.
    """

    content = read_file(file_path)

    response = ollama.chat(
        model=DEFAULT_MODEL,
        messages=[
            {
                "role": "user",
                "content": f"{SUMMARY_PROMPT}\n\n{content}"
            }
        ]
    )

    return SummaryResult(
        file_name=file_path,
        summary=response["message"]["content"],
        model=DEFAULT_MODEL
    )


def scan_current_project(path: str = ".") -> ProjectScanResult:
    """
    Scan the specified project directory.
    Defaults to the current directory.
    """
    return scan_project(path)


def index_project(path: str = ".") -> str:
    """
    Scan a project and generate an index file.
    """

    scan = scan_current_project(path)

    index_path = create_index(scan)

    return str(index_path)


def project_summary(path: str = ".") -> str:
    """
    Generate an AI summary of a project using its indexed metadata
    and important project files.
    """

    context = build_project_context(path)

    response = ollama.chat(
        model=DEFAULT_MODEL,
        messages=[
            {
                "role": "user",
                "content": (
                    f"{PROJECT_SUMMARY_PROMPT}\n\n"
                    f"{context}"
                ),
            }
        ],
    )

    return response["message"]["content"]