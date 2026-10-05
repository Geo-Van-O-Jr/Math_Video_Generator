from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROFILES = {
    "preview": {"resolution": "854,480", "fps": 15},
    "final": {"resolution": "1920,1080", "fps": 60},
}
