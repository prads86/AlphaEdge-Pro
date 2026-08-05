from app.brokers.broker_service import BrokerService

broker = BrokerService()

print()

print("Connected :", broker.is_connected())

print()

profile = broker.profile()

print("User Name :", profile["user_name"])
print("User ID   :", profile["user_id"])
print("Email     :", profile["email"])

print()

print("Margins")

print(broker.margins())