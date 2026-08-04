from app.brokers.zerodha import get_client
from app.config.settings import KITE_API_SECRET

def generate_access_token(request_token: str):
    kite = get_client()

    session = kite.generate_session(
        request_token=request_token,
        api_secret=KITE_API_SECRET,
    )

    return session