"""
tick_cache.py

Thread-safe singleton cache for live market data.
"""

from collections import deque
from copy import deepcopy
from datetime import datetime
from threading import Lock


class TickCache:
    """
    Singleton cache for the latest market ticks.

    Every module in AlphaEdge Pro shares the same instance.
    """

    _instance = None
    _instance_lock = Lock()

    def __new__(cls):
        with cls._instance_lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)

                cls._instance._ticks = {}
                cls._instance._history = {}
                cls._instance._lock = Lock()
                cls._instance._last_update = None

        return cls._instance

    def update(self, ticks):
        """
        Update the cache with incoming WebSocket ticks.
        """

        with self._lock:

            now = datetime.now()

            for tick in ticks:

                token = tick["instrument_token"]

                # Store latest tick
                self._ticks[token] = tick

                # Keep rolling history (last 100 ticks)
                if token not in self._history:
                    self._history[token] = deque(maxlen=100)

                self._history[token].append(deepcopy(tick))

            self._last_update = now

    def get(self, instrument_token):
        """
        Returns the latest tick for an instrument.
        """

        with self._lock:
            return self._ticks.get(instrument_token)

    def get_history(self, instrument_token):
        """
        Returns the recent tick history.
        """

        with self._lock:

            if instrument_token not in self._history:
                return []

            return list(self._history[instrument_token])

    def latest_price(self, instrument_token):
        """
        Returns the latest traded price.
        """

        tick = self.get(instrument_token)

        if tick is None:
            return None

        return tick.get("last_price")

    def get_all(self):
        """
        Returns all latest ticks.
        """

        with self._lock:
            return dict(self._ticks)

    def clear(self):
        """
        Clears the cache.
        """

        with self._lock:

            self._ticks.clear()
            self._history.clear()
            self._last_update = None

    @property
    def count(self):
        with self._lock:
            return len(self._ticks)

    @property
    def last_update(self):
        return self._last_update