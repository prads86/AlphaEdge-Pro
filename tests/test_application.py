from app.core.application import AlphaEdgeApplication

app = AlphaEdgeApplication()

app.start()

print()

print("Broker Loaded      :", app.broker is not None)
print("Market Loaded      :", app.market is not None)
print("Repository Loaded  :", app.instruments is not None)