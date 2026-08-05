"""
broker_service.py

Central Broker Service for AlphaEdge Pro.

Responsibilities
----------------
- Maintain a single authenticated KiteConnect client
- Expose broker APIs
- Validate session
- Serve as the only broker interface used by the application
"""

from kiteconnect import KiteConnect

from app.config.settings import KITE_API_KEY
from app.brokers.session_manager import SessionManager
from app.utils.logger import log


class BrokerService:
    """
    Singleton wrapper around KiteConnect.
    """

    _instance = None

    def __new__(cls):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

            cls._instance._initialize()

        return cls._instance

    def _initialize(self):

        self.session = SessionManager()

        access_token = self.session.get_access_token()

        if not access_token:
            raise RuntimeError(
                "No Zerodha access token found. Please login first."
            )

        self.kite = KiteConnect(api_key=KITE_API_KEY)
        self.kite.set_access_token(access_token)

        log.info("BrokerService initialized successfully.")

    @property
    def client(self):
        """
        Returns the authenticated KiteConnect client.
        """
        return self.kite

    # --------------------------------------------------
    # Account APIs
    # --------------------------------------------------

    def profile(self):
        return self.kite.profile()

    def margins(self):
        return self.kite.margins()

    def holdings(self):
        return self.kite.holdings()

    def positions(self):
        return self.kite.positions()

    def orders(self):
        return self.kite.orders()

    # --------------------------------------------------
    # Market APIs
    # --------------------------------------------------

    def instruments(self):
        return self.kite.instruments()

    def quote(self, instruments):
        return self.kite.quote(instruments)

    def ltp(self, instruments):
        return self.kite.ltp(instruments)

    # --------------------------------------------------
    # Trading APIs
    # --------------------------------------------------

    def place_order(self, **kwargs):
        """
        Wrapper around KiteConnect.place_order().
        """
        log.info("Placing order...")

        return self.kite.place_order(**kwargs)

    def modify_order(self, **kwargs):
        return self.kite.modify_order(**kwargs)

    def cancel_order(self, variety, order_id):
        return self.kite.cancel_order(
            variety=variety,
            order_id=order_id,
        )

    # --------------------------------------------------
    # Health Check
    # --------------------------------------------------

    def is_connected(self):
        """
        Checks whether the current session is valid.
        """
        try:
            self.profile()
            return True
        except Exception as ex:
            log.error("Broker connection failed: {}", ex)
            return False