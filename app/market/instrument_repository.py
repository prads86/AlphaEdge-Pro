"""
instrument_repository.py

Repository for querying instruments stored in DuckDB.
"""

from app.database.duckdb_service import DuckDBService
from app.utils.logger import log


class InstrumentRepository:
    """
    Repository for looking up instruments.
    """

    _instance = None

    def __new__(cls):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

            cls._instance.db = DuckDBService().connection

        return cls._instance

    def count(self):

        return self.db.execute(
            "SELECT COUNT(*) FROM instruments"
        ).fetchone()[0]

    def get_token(self, symbol: str, exchange: str = "NSE"):

        row = self.db.execute(
            """
            SELECT instrument_token
            FROM instruments
            WHERE tradingsymbol = ?
              AND exchange = ?
            LIMIT 1
            """,
            [symbol, exchange],
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
                segment,
                instrument_type
            FROM instruments
            WHERE
                UPPER(tradingsymbol) LIKE UPPER(?)
                OR UPPER(name) LIKE UPPER(?)
            ORDER BY tradingsymbol
            LIMIT ?
            """,
            [f"%{text}%", f"%{text}%", limit],
        ).fetchdf()

    def get_watchlist_tokens(self, symbols, exchange="NSE"):

        tokens = []

        for symbol in symbols:

            token = self.get_token(symbol, exchange)

            if token:

                tokens.append(token)

            else:

                log.warning(
                    "Instrument not found: {} ({})",
                    symbol,
                    exchange,
                )

        return tokens

    def exists(self, symbol: str, exchange="NSE"):

        return self.get_token(symbol, exchange) is not None