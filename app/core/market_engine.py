"""
market_engine.py

Runs the live market feed for AlphaEdge Pro.
"""

from app.brokers.websocket_service import WebSocketService
from app.market.instrument_repository import InstrumentRepository
from app.config.settings import settings
from app.utils.logger import log


class MarketEngine:

    def __init__(self):

        self.repo = InstrumentRepository()
        self.websocket = WebSocketService()

    def start(self):

        watchlist = (
            settings.market
            .get("watchlist", {})
            .get("equities", [])
        )

        tokens = self.repo.get_watchlist_tokens(watchlist)

        log.info(
            "Starting Market Engine with {} instruments.",
            len(tokens),
        )

        def on_connect(ws, response):

            log.info("Connected to Zerodha WebSocket")

            self.websocket.subscribe(tokens)

        self.websocket.kws.on_connect = on_connect

        self.websocket.connect()