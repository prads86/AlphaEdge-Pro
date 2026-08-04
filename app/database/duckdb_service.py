from pathlib import Path
import duckdb

class DuckDBService:
    def __init__(self, db_path='data/market.duckdb'):
        Path('data').mkdir(exist_ok=True)
        self.conn=duckdb.connect(db_path)
    @property
    def connection(self):
        return self.conn