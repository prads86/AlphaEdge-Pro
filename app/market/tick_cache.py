"""
tick_cache.py

Thread-safe in-memory cache for live market ticks.
"""

from threading import Lock
from datetime import datetime


class TickCache:
    def __init__(self):
        self._ticks = {}
        self._lock = Lock()
        self._last_update = None

    def update(self, ticks):
        """
        Update the cache with a list of ticks received
        from the Zerodha WebSocket.
        """
        with self._lock:
            for tick in ticks:
                token = tick["instrument_token"]
                self._ticks[token] = tick

            self._last_update = datetime.now()

    def get(self, instrument_token):
        with self._lock:
            return self._ticks.get(instrument_token)

    def get_all(self):
        with self._lock:
            return dict(self._ticks)

    @property
    def count(self):
        with self._lock:
            return len(self._ticks)

    @property
    def last_update(self):
        return self._last_update