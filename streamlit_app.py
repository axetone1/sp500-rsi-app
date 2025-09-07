import pandas as pd
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(layout="wide")

st.title("📈 S&P 500 RSI Vizualizáció")

# CSV betöltése
@st.cache_data
def load_data():
    return pd.read_csv("sp500_rsi_daily_2020_to_today.csv", index_col=0, parse_dates=True)

df = load_data()

# Cégek listája
tickers = df.columns.tolist()
selected_ticker = st.selectbox("Válassz céget:", tickers)

# Dátum szűrés
start_date = st.date_input("Kezdő dátum", value=df.index.min().date())
end_date = st.date_input("Záró dátum", value=df.index.max().date())

# Szűrés
filtered_df = df.loc[(df.index >= pd.to_datetime(start_date)) & (df.index <= pd.to_datetime(end_date))]

# Grafikon
fig = go.Figure()
fig.add_trace(go.Scatter(x=filtered_df.index, y=filtered_df[selected_ticker], mode='lines', name=selected_ticker))
fig.update_layout(title=f"{selected_ticker} RSI", yaxis=dict(range=[0, 100]), template="plotly_dark")

st.plotly_chart(fig, use_container_width=True)
