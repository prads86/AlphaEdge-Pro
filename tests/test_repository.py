from app.market.instrument_repository import InstrumentRepository

repo = InstrumentRepository()

print()

print("Instrument Count:", repo.count())

print()

symbols = [
    "RELIANCE",
    "INFY",
    "SBIN",
    "ICICIBANK",
    "TCS",
]

tokens = repo.get_watchlist_tokens(symbols)

for symbol, token in zip(symbols, tokens):
    print(f"{symbol:<15} {token}")

print()

print(repo.search("TATA"))