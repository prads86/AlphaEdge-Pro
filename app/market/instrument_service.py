from app.database.duckdb_service import DuckDBService
class InstrumentRepository:
    def __init__(self):
        self.db=DuckDBService().connection
    def get_token(self,symbol):
        r=self.db.execute('SELECT instrument_token FROM instruments WHERE tradingsymbol=? LIMIT 1',[symbol]).fetchone()
        return r[0] if r else None