from app.config.settings import KITE_API_KEY
from app.brokers.session_manager import SessionManager
from kiteconnect import KiteConnect

print("API Key:", KITE_API_KEY)

token = SessionManager().get_access_token()

print("Token starts with:", token[:10])

kite = KiteConnect(api_key=KITE_API_KEY)
kite.set_access_token(token)

print("\nCalling profile()...")

print(kite.profile())