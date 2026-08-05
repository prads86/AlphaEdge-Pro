"""
market_store.py

Persists live market ticks into DuckDB.
"""

from datetime import datetime

from app.database.duckdb_service import DuckDBService
from app.utils.logger import log


class MarketStore:
    _instance = None

    def __new__(cls):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

            cls._instance.db = DuckDBService().connection

            cls._instance._create_table()

        return cls._instance

    def _create_table(self):

        self.db.execute("""
        CREATE TABLE IF NOT EXISTS live_ticks (

            timestamp TIMESTAMP,

            instrument_token BIGINT,

            last_price DOUBLE,

            volume BIGINT,

            oi BIGINT,

            bid DOUBLE,

            ask DOUBLE

        )
        """)

    def save_ticks(self, ticks):

        if not ticks:
            return

        now = datetime.now()

        rows = []

        for tick in ticks:

            depth = tick.get("depth", {})

            buy = depth.get("buy", [])
            sell = depth.get("sell", [])

            bid = buy[0]["price"] if buy else None
            ask = sell[0]["price"] if sell else None

            rows.append(
                (
                    now,
                    tick["instrument_token"],
                    tick.get("last_price"),
                    tick.get("volume"),
                    tick.get("oi"),
                    bid,
                    ask,
                )
            )

        self.db.executemany(
            """
            INSERT INTO live_ticks
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            rows,
        )

        log.debug(
            "Stored {} live ticks.",
            len(rows),
        )

    def latest_ticks(self, limit=20):

        return self.db.execute(
            """
            SELECT *
            FROM live_ticks
            ORDER BY timestamp DESC
            LIMIT ?
            """,
            [limit],
        ).fetchdf()