from app.market.tick_cache import TickCache

cache1 = TickCache()
cache2 = TickCache()

print("Same instance:", cache1 is cache2)

cache1.update([
    {
        "instrument_token": 12345,
        "last_price": 100.5,
        "volume": 1000,
    }
])

print()

print("Latest Price :", cache2.latest_price(12345))
print("History Size :", len(cache2.get_history(12345)))
print("Cached Items :", cache2.count)