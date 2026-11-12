import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load_problems(path=None):
    source = Path(path) if path else ROOT / "data" / "problems.json"
    problems = json.loads(source.read_text(encoding="utf-8"))
    if not isinstance(problems, list) or not problems:
        raise ValueError("Dataset must be a non-empty JSON list")
    for p in problems:
        for key in ("id", "name", "description", "category", "tests"):
            if key not in p: raise ValueError(f"Problem missing {key}: {p}")
        if not p["tests"]: raise ValueError(f"Problem {p['id']} has no tests")
    return problems
