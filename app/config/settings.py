"""
settings.py

Central configuration for AlphaEdge Pro.
"""

from pathlib import Path
import yaml


BASE_DIR = Path(__file__).resolve().parents[2]
CONFIG_FILE = BASE_DIR / "config.yaml"


class Settings:

    _instance = None

    def __new__(cls):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

            cls._instance.reload()

        return cls._instance

    def reload(self):

        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            self.config = yaml.safe_load(f)

    @property
    def app(self):
        return self.config.get("app", {})

    @property
    def database(self):
        return self.config.get("database", {})

    @property
    def scanner(self):
        return self.config.get("scanner", {})

    @property
    def alerts(self):
        return self.config.get("alerts", {})

    @property
    def market(self):
        return self.config.get("market", {})


settings = Settings()


# ------------------------------------------------------
# Backward compatibility
# ------------------------------------------------------

KITE_API_KEY = settings.config.get("zerodha", {}).get("api_key")
KITE_API_SECRET = settings.config.get("zerodha", {}).get("api_secret")