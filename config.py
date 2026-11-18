import json
from pathlib import Path

PROFILE_PATH = Path("config/candidate.local.json")

def load_candidate() -> dict:
    if not PROFILE_PATH.exists():
        raise FileNotFoundError(
            f"Create {PROFILE_PATH} from config/candidate.example.json first."
        )
    return json.loads(PROFILE_PATH.read_text(encoding="utf-8"))
