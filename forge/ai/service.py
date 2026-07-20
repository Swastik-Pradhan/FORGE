import ollama

from forge.ai.prompts import SUMMARY_PROMPT
from forge.ai.models import SummaryResult
from forge.utils.files import read_file
from forge.utils.config import DEFAULT_MODEL


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