from pathlib import Path
import os

from dotenv import load_dotenv
import yaml

BASE_DIR = Path(__file__).resolve().parents[2]

load_dotenv(BASE_DIR / ".env")

CONFIG_FILE = BASE_DIR / "config.yaml"


def load_config():
    with open(CONFIG_FILE, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


config = load_config()

KITE_API_KEY = os.getenv("KITE_API_KEY")
KITE_API_SECRET = os.getenv("KITE_API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")