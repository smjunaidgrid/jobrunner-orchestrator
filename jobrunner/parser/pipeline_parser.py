import yaml
from pathlib import Path

def parse_pipeline(file_path: str):
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Pipeline file not found: {file_path}")

    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if not isinstance(data, dict):
        raise ValueError("Pipeline file must contain a YAML object")

    if "name" not in data:
        raise ValueError("Pipeline must have a 'name' field")

    if "steps" not in data:
        raise ValueError("Pipeline must contain 'steps'")

    if not isinstance(data["steps"], list) or not data["steps"]:
        raise ValueError("Pipeline 'steps' must be a non-empty list")

    for step in data["steps"]:
        if "name" not in step:
            raise ValueError("Each step must have a 'name'")
        if "command" not in step:
            raise ValueError("Each step must have a 'command'")
        step.setdefault("retry", 0)

    return data
