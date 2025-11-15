import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Gold SIP Calculator", layout="wide")
st.title("🏆 Gold SIP Calculator with Date-wise Graph")

# ---- INPUTS ----
monthly_investment = st.number_input("📥 Monthly Investment (₹)", min_value=0.0, value=2000.0)
years = st.number_input("📅 Investment Duration (Years)", min_value=1, value=10)
expected_growth = st.number_input("📈 Expected Annual Gold Price Growth (%)", min_value=0.0, value=8.0)

months = int(years * 12)
monthly_rate = expected_growth / 12 / 100

# ---- DATE RANGE ----
dates = pd.date_range(start=pd.Timestamp.today(), periods=months, freq="M")

# ---- SIP CALCULATION ----
corpus = []
invested = []
c = 0
inv = 0

for _ in range(months):
    inv += monthly_investment
    c = c * (1 + monthly_rate) + monthly_investment
    invested.append(inv)
    corpus.append(c)

# ---- DATAFRAME ----
df = pd.DataFrame({
    "Date": dates,
    "Invested": invested,
    "Corpus": corpus
})

# ---- RESULTS ----
st.subheader("📊 Results")
st.success(f"Projected Gold SIP Corpus: ₹{corpus[-1]:,.2f}")
st.info(f"Total Invested: ₹{inv:,.2f}")
st.info(f"Profit: ₹{corpus[-1] - inv:,.2f}")

# ---- DATE-WISE GRAPH ----
st.subheader("📉 Gold SIP Growth Over Time (With Dates)")
st.line_chart(df.set_index("Date")[["Invested", "Corpus"]])

# ---- TABLE ----
st.subheader("📘 Detailed SIP Table")
st.dataframe(df)
