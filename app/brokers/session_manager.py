import json
from pathlib import Path


class SessionManager:
    def __init__(self):
        self.session_file = Path("secrets/session.json")

    def load(self):
        if not self.session_file.exists():
            raise FileNotFoundError(
                "session.json not found. Please login first."
            )

        with open(self.session_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def get_access_token(self):
        session = self.load()

        token = session.get("access_token")

        if not token:
            raise Exception("Access token missing.")

        return token