from time import sleep

from app.market.market_data_service import MarketDataService

market = MarketDataService()

market.clear()

market.process_ticks([
    {
        "instrument_token": 12345,
        "last_price": 100.25,
        "volume": 100,
    }
])

sleep(1)

market.process_ticks([
    {
        "instrument_token": 12345,
        "last_price": 101.75,
        "volume": 250,
    }
])

print()

print("Latest Price      :", market.latest_price(12345))
print("History Length    :", len(market.tick_history(12345)))
print("Cached Instruments:", market.cached_instruments)
print("Total Ticks       :", market.total_ticks)
print("Messages          :", market.total_messages)
print("Ticks / Second    :", market.ticks_per_second)
print("Messages / Second :", market.messages_per_second)