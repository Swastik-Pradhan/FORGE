from dataclasses import dataclass

@dataclass
class SummaryResult:
    file_name: str
    summary: str
    model: str