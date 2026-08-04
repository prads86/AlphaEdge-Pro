from app.market.tick_cache import TickCache

cache = TickCache()

sample_tick = {
    "instrument_token": 256265,
    "last_price": 25123.45,
    "volume": 123456,
}

cache.update([sample_tick])

print("Cached Instruments:", cache.count)
print(cache.get(256265))