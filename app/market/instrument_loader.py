from datetime import datetime
import pandas as pd
from app.brokers.broker_service import BrokerService
from app.database.duckdb_service import DuckDBService

class InstrumentLoader:
    def __init__(self):
        self.db=DuckDBService().connection
        self.db.execute('CREATE TABLE IF NOT EXISTS instruments(instrument_token BIGINT,exchange_token BIGINT,tradingsymbol VARCHAR,name VARCHAR,last_price DOUBLE,expiry DATE,strike DOUBLE,tick_size DOUBLE,lot_size INTEGER,instrument_type VARCHAR,segment VARCHAR,exchange VARCHAR,updated_at TIMESTAMP)')
    def refresh(self):
        df=pd.DataFrame(BrokerService().client.instruments())
        df['expiry']=pd.to_datetime(df['expiry'],errors='coerce')
        for c in ['strike','last_price','tick_size']:
            df[c]=pd.to_numeric(df[c],errors='coerce')
        df['lot_size']=pd.to_numeric(df['lot_size'],errors='coerce').fillna(0).astype(int)
        df['updated_at']=datetime.now()
        cols=['instrument_token','exchange_token','tradingsymbol','name','last_price','expiry','strike','tick_size','lot_size','instrument_type','segment','exchange','updated_at']
        df=df[cols]
        self.db.execute('DELETE FROM instruments')
        self.db.register('instrument_df',df)
        self.db.execute('INSERT INTO instruments SELECT * FROM instrument_df')
        return len(df)