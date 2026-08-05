from app.market.tick_cache import TickCache

cache1 = TickCache()
cache2 = TickCache()

print("Same instance:", cache1 is cache2)

cache1.update([
    {
        "instrument_token": 12345,
        "last_price": 100.5
    }
])

print(cache2.get(12345))