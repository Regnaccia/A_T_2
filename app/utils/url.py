from pathlib import Path

def resolve_path(base_path: Path, relative_path: str) -> Path:
    return base_path / relative_path