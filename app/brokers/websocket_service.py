"""
websocket_service.py

Receives live ticks from Zerodha and stores them in TickCache.
"""

from kiteconnect import KiteTicker

from app.config.settings import KITE_API_KEY
from app.brokers.session_manager import SessionManager
from app.market.tick_cache import TickCache


class WebSocketService:

    def __init__(self):

        self.cache = TickCache()

        access_token = SessionManager().get_access_token()

        self.kws = KiteTicker(
            KITE_API_KEY,
            access_token,
        )

        self.connected = False

        self._register_callbacks()

    def _register_callbacks(self):

        self.kws.on_connect = self.on_connect
        self.kws.on_ticks = self.on_ticks
        self.kws.on_close = self.on_close
        self.kws.on_error = self.on_error

    def on_connect(self, ws, response):

        self.connected = True

        print("✅ Connected to Zerodha WebSocket")

    def on_ticks(self, ws, ticks):

        self.cache.update(ticks)

        print(
            f"Received {len(ticks)} ticks | "
            f"Cached: {self.cache.count}"
        )

    def on_close(self, ws, code, reason):

        self.connected = False

        print(f"WebSocket closed ({code}) {reason}")

    def on_error(self, ws, code, reason):

        print(f"WebSocket error ({code}) {reason}")

    def subscribe(self, instrument_tokens):

        self.kws.subscribe(instrument_tokens)

        self.kws.set_mode(
            self.kws.MODE_FULL,
            instrument_tokens,
        )

    def connect(self):

        self.kws.connect(threaded=False)