from dataclasses import dataclass, field, asdict


@dataclass
class SummaryResult:
    file_name: str
    summary: str
    model: str


@dataclass
class ProjectScanResult:
    """
    Stores information gathered during a project scan.
    """

    project_name: str
    root_path: str

    total_files: int
    total_directories: int

    total_size: int

    largest_file: str
    largest_file_size: int

    file_types: dict[str, int] = field(default_factory=dict)

    files: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        """
        Convert the project scan result into a dictionary.
        """
        return asdict(self)