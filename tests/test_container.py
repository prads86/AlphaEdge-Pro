from app.core.container import ServiceContainer

c1 = ServiceContainer()
c2 = ServiceContainer()

print("Same container:", c1 is c2)

print("Same broker:", c1.broker is c2.broker)

print("Same cache:", c1.tick_cache is c2.tick_cache)

print("Same market:", c1.market_data is c2.market_data)

print("Same repository:", c1.instrument_repository is c2.instrument_repository)