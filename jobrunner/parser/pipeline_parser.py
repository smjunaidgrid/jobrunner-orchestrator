import yaml
from pathlib import Path

def parse_pipeline(file_path: str):
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(file_path)

    with open(path) as f:
        data = yaml.safe_load(f)

    if "name" not in data or "steps" not in data:
        raise ValueError("Invalid pipeline format")

    for step in data["steps"]:
        step.setdefault("retry", 0)

    return data