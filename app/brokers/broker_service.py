"""
broker_service.py

Centralized Zerodha broker service.

Every module in AlphaEdge Pro should use this class instead of
creating KiteConnect objects directly.
"""

from kiteconnect import KiteConnect

from app.config.settings import KITE_API_KEY
from app.brokers.session_manager import SessionManager


class BrokerService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            kite = KiteConnect(api_key=KITE_API_KEY)

            access_token = SessionManager().get_access_token()

            kite.set_access_token(access_token)

            cls._instance._kite = kite

        return cls._instance

    @property
    def client(self):
        return self._kite

    def profile(self):
        return self._kite.profile()

    def margins(self):
        return self._kite.margins()

    def holdings(self):
        return self._kite.holdings()

    def positions(self):
        return self._kite.positions()

    def instruments(self):
        return self._kite.instruments()