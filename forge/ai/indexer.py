from pathlib import Path

from forge.ai.models import ProjectScanResult
from forge.utils.json_utils import write_json


INDEX_DIRECTORY = ".forge"
INDEX_FILE = "index.json"


def create_index(scan: ProjectScanResult) -> Path:
    """
    Create a project index from a project scan.
    """

    project_root = Path(scan.root_path)

    index_path = (
        project_root /
        INDEX_DIRECTORY /
        INDEX_FILE
    )

    write_json(
        index_path,
        scan.to_dict()
    )

    return index_path