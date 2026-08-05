"""
container.py

Central dependency container for AlphaEdge Pro.
"""

from app.brokers.broker_service import BrokerService
from app.market.tick_cache import TickCache
from app.market.market_data_service import MarketDataService
from app.market.instrument_repository import InstrumentRepository


class ServiceContainer:
    _instance = None

    def __new__(cls):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

            cls._instance.broker = BrokerService()
            cls._instance.tick_cache = TickCache()
            cls._instance.market_data = MarketDataService()
            cls._instance.instrument_repository = InstrumentRepository()

        return cls._instance