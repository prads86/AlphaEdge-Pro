from kiteconnect import KiteConnect
from app.config.settings import KITE_API_KEY

kite = KiteConnect(api_key=KITE_API_KEY)

def get_login_url():
    return kite.login_url()