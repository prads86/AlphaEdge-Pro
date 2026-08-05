from app.brokers.session_manager import SessionManager

session = SessionManager()

print(session.get_access_token())