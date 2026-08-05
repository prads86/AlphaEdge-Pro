"""
market_data_service.py

Central processing pipeline for live market data.
"""

from datetime import datetime

from app.market.tick_cache import TickCache
from app.utils.logger import log
from app.market.market_store import MarketStore

class MarketDataService:
    """
    Processes all incoming market ticks before they are stored.

    Responsibilities:
        - Update TickCache
        - Maintain statistics
        - Provide market data access
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            cls._instance.cache = TickCache()

            cls._instance.store = MarketStore()

            cls._instance.start_time = datetime.now()

            cls._instance.total_ticks = 0

            cls._instance.total_messages = 0

            cls._instance.last_tick_time = None

        return cls._instance

    def process_ticks(self, ticks):
        """
        Process a batch of WebSocket ticks.
        """

        if not ticks:
            return

        self.total_messages += 1
        self.total_ticks += len(ticks)

        self.last_tick_time = datetime.now()

        self.cache.update(ticks)

        self.store.save_ticks(ticks)

        log.debug(
            "Processed {} ticks (Total: {})",
            len(ticks),
            self.total_ticks,
        )

    @property
    def cached_instruments(self):
        return self.cache.count

    @property
    def last_update(self):
        return self.cache.last_update

    @property
    def uptime_seconds(self):

        return (
            datetime.now() - self.start_time
        ).total_seconds()

    @property
    def ticks_per_second(self):

        uptime = self.uptime_seconds

        if uptime <= 0:
            return 0.0

        return round(
            self.total_ticks / uptime,
            2,
        )

    @property
    def messages_per_second(self):

        uptime = self.uptime_seconds

        if uptime <= 0:
            return 0.0

        return round(
            self.total_messages / uptime,
            2,
        )

    def latest_price(self, instrument_token):

        return self.cache.latest_price(
            instrument_token
        )

    def latest_tick(self, instrument_token):

        return self.cache.get(
            instrument_token
        )

    def tick_history(self, instrument_token):

        return self.cache.get_history(
            instrument_token
        )

    def all_ticks(self):

        return self.cache.get_all()

    def clear(self):

        self.cache.clear()

        self.total_ticks = 0

        self.total_messages = 0

        self.last_tick_time = None

        self.start_time = datetime.now()

        log.info("MarketDataService reset.")