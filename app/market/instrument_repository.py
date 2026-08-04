from app.database.duckdb_service import DuckDBService


class InstrumentRepository:
    def __init__(self):
        self.db = DuckDBService().connection

    def get_token(self, symbol: str):
        row = self.db.execute(
            """
            SELECT instrument_token
            FROM instruments
            WHERE tradingsymbol = ?
            LIMIT 1
            """,
            [symbol],
        ).fetchone()

        return row[0] if row else None

    def get_symbol(self, token: int):
        row = self.db.execute(
            """
            SELECT tradingsymbol
            FROM instruments
            WHERE instrument_token = ?
            LIMIT 1
            """,
            [token],
        ).fetchone()

        return row[0] if row else None

    def search(self, text: str, limit: int = 20):
        return self.db.execute(
            """
            SELECT
                tradingsymbol,
                name,
                exchange,
                segment
            FROM instruments
            WHERE UPPER(tradingsymbol) LIKE UPPER(?)
               OR UPPER(name) LIKE UPPER(?)
            LIMIT ?
            """,
            [f"%{text}%", f"%{text}%", limit],
        ).fetchdf()