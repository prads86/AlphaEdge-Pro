from app.brokers.websocket_service import WebSocketService
from app.market.instrument_repository import InstrumentRepository


repo = InstrumentRepository()

tokens = [
    repo.get_token("RELIANCE"),
    repo.get_token("INFY"),
    repo.get_token("SBIN"),
]

ws = WebSocketService()


def on_connect(socket, response):
    print("Subscribing...")
    ws.subscribe(tokens)


# Replace the default callback with our subscription callback
ws.kws.on_connect = on_connect

print("Starting WebSocket...")

ws.connect()