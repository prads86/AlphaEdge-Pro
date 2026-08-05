"""
websocket_service.py

Receives live ticks from Zerodha and forwards them to the
MarketDataService.
"""

from kiteconnect import KiteTicker

from app.config.settings import KITE_API_KEY
from app.brokers.session_manager import SessionManager
from app.market.market_data_service import MarketDataService
from app.utils.logger import log


class WebSocketService:
    """
    Manages the Zerodha KiteTicker WebSocket connection.
    """

    def __init__(self):

        self.market = MarketDataService()

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

        log.info("Connected to Zerodha WebSocket")

    def on_ticks(self, ws, ticks):

        self.market.process_ticks(ticks)

        log.info(
            "Received {} ticks | Cached Instruments: {}",
            len(ticks),
            self.market.cached_instruments,
        )

    def on_close(self, ws, code, reason):

        self.connected = False

        log.warning(
            "WebSocket closed | Code: {} | Reason: {}",
            code,
            reason,
        )

    def on_error(self, ws, code, reason):

        log.error(
            "WebSocket error | Code: {} | Reason: {}",
            code,
            reason,
        )

    def subscribe(self, instrument_tokens):

        self.kws.subscribe(instrument_tokens)

        self.kws.set_mode(
            self.kws.MODE_FULL,
            instrument_tokens,
        )

        log.info(
            "Subscribed to {} instruments",
            len(instrument_tokens),
        )

    def connect(self):

        log.info("Starting Zerodha WebSocket...")

        self.kws.connect(threaded=False)