from pprint import pprint

from app.brokers.broker_service import BrokerService
from app.market.instrument_loader import InstrumentLoader
from app.market.instrument_repository import InstrumentRepository


def main():
    print("=" * 70)
    print("AlphaEdge Pro - Module 3 Foundation")
    print("=" * 70)

    # ------------------------------------------------------------------
    # Verify Zerodha connection
    # ------------------------------------------------------------------

    broker = BrokerService()

    profile = broker.profile()

    print("\n✅ Connected to Zerodha\n")

    pprint(
        {
            "User": profile.get("user_name"),
            "User ID": profile.get("user_id"),
            "Email": profile.get("email"),
            "Broker": "Zerodha",
        }
    )

    # ------------------------------------------------------------------
    # Load instrument master
    # ------------------------------------------------------------------

    loader = InstrumentLoader()

    count = loader.refresh()

    print(f"\n✅ Loaded {count:,} instruments into DuckDB")

    # ------------------------------------------------------------------
    # Query instrument repository
    # ------------------------------------------------------------------

    repo = InstrumentRepository()

    symbols = [
        "RELIANCE",
        "INFY",
        "SBIN",
        "ICICIBANK",
        "TCS",
    ]

    print("\nInstrument Tokens")
    print("-" * 70)

    for symbol in symbols:
        token = repo.get_token(symbol)
        print(f"{symbol:<15} {token}")

    print("\n✅ Module 3 Foundation completed successfully.")


if __name__ == "__main__":
    main()