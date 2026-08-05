import streamlit as st
import pandas as pd
from datetime import datetime

from app.market.tick_cache import TickCache

st.set_page_config(
    page_title="AlphaEdge Pro",
    page_icon="📈",
    layout="wide"
)

st.title("📈 AlphaEdge Pro")
st.caption("Live Market Dashboard")

cache = TickCache()

st.subheader("System Status")

col1, col2, col3 = st.columns(3)

col1.metric("Cached Instruments", cache.count)

last_update = cache.last_update
col2.metric(
    "Last Update",
    last_update.strftime("%H:%M:%S") if last_update else "-"
)

status = "🟢 Connected" if cache.count > 0 else "🟡 Waiting"
col3.metric("Market Feed", status)

st.divider()

ticks = cache.get_all()

if ticks:
    rows = []

    for tick in ticks.values():
        rows.append({
            "Token": tick.get("instrument_token"),
            "Price": tick.get("last_price"),
            "Volume": tick.get("volume", 0),
        })

    df = pd.DataFrame(rows)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
    )
else:
    st.info("Waiting for live market data...")