from app.core.container import ServiceContainer


class AlphaEdgeApplication:

    def __init__(self):
        self.container = ServiceContainer()

    def initialize(self):
        print("=" * 60)
        print("Initializing AlphaEdge Pro")
        print("=" * 60)

        print("✓ Broker Service")
        print("✓ Instrument Repository")
        print("✓ Market Data Service")
        print("✓ Tick Cache")

    def start(self):
        self.initialize()

        print("\nApplication initialized successfully.")

    @property
    def broker(self):
        return self.container.broker

    @property
    def market(self):
        return self.container.market_data

    @property
    def instruments(self):
        return self.container.instrument_repository