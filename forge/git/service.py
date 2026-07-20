import subprocess
import ollama

from forge.utils.config import DEFAULT_MODEL


def is_git_repository() -> bool:
    """
    Check if the current directory is a git repository.
    """
    result = subprocess.run(
        ["git", "rev-parse", "--is-inside-work-tree"],
        capture_output=True,
        text=True,
    )

    return result.returncode == 0


def get_git_status() -> str:
    """
    Return git status.
    """
    result = subprocess.run(
        ["git", "status"],
        capture_output=True,
        text=True,
    )

    return result.stdout


def get_git_diff() -> str:
    """
    Return unstaged git diff.
    """
    result = subprocess.run(
        ["git", "diff"],
        capture_output=True,
        text=True,
    )

    return result.stdout


def generate_commit_message() -> str:
    """
    Generate a commit message using Ollama.
    """

    diff = get_git_diff()

    if not diff.strip():
        return "No changes detected."

    response = ollama.chat(
        model=DEFAULT_MODEL,
        messages=[
            {
                "role": "user",
                "content": f"""
Generate a concise Git commit message
using Conventional Commits.

Git diff:

{diff}
"""
            }
        ],
    )

    return response["message"]["content"]