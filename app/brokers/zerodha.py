from kiteconnect import KiteConnect
from app.config.settings import KITE_API_KEY

def get_client():
    return KiteConnect(api_key=KITE_API_KEY)