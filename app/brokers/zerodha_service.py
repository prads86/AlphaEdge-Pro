from kiteconnect import KiteConnect

from app.config.settings import KITE_API_KEY
from app.brokers.session_manager import SessionManager


class ZerodhaService:

    def __init__(self):
        self.kite = KiteConnect(api_key=KITE_API_KEY)

        access_token = SessionManager().get_access_token()

        self.kite.set_access_token(access_token)

    def profile(self):
        return self.kite.profile()

    def margins(self):
        return self.kite.margins()

    def holdings(self):
        return self.kite.holdings()

    def client(self):
        return self.kite