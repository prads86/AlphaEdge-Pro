import json
import webbrowser
from pathlib import Path
from flask import Flask, request
from app.brokers.zerodha import get_client
from app.config.settings import KITE_API_SECRET

app = Flask(__name__)

SECRETS = Path("secrets")
SECRETS.mkdir(exist_ok=True)
SESSION_FILE = SECRETS / "session.json"

@app.route("/")
def callback():
    request_token = request.args.get("request_token")
    if not request_token:
        return "Missing request_token", 400

    kite = get_client()
    session = kite.generate_session(
        request_token=request_token,
        api_secret=KITE_API_SECRET,
    )

    SESSION_FILE.write_text(
    json.dumps(session, indent=2, default=str)
)
    return "Login successful. You may close this window."

if __name__ == "__main__":
    kite = get_client()
    print("Opening Zerodha login...")
    webbrowser.open(kite.login_url())
    app.run(host="127.0.0.1", port=8000)