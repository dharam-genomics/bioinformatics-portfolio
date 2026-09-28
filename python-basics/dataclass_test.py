from dataclasses import dataclass


@dataclass
class QCResult:
    reads: int | None
    status: str
    error: str | None = None


result = QCResult(
    reads=8,
    status="PASS"
)

print(result)
