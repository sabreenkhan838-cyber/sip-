import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Gold SIP Calculator", layout="wide")
st.title("🏆 Gold SIP Calculator with Graph (No Matplotlib)")

monthly_investment = st.number_input("📥 Monthly Investment (₹)", min_value=0.0, value=2000.0)
years = st.number_input("📅 Investment Duration (Years)", min_value=1, value=10)
expected_growth = st.number_input("📈 Expected Annual Gold Growth (%)", min_value=0.0, value=8.0)

months = int(years * 12)
monthly_rate = expected_growth / 12 / 100

corpus = []
invested = []
c = 0
inv = 0

for i in range(months):
    inv += monthly_investment
    c = c * (1 + monthly_rate) + monthly_investment
    corpus.append(c)
    invested.append(inv)

df = pd.DataFrame({
    "Month": range(1, months + 1),
    "Invested": invested,
    "Corpus": corpus
})

st.success(f"Projected Corpus: ₹{corpus[-1]:,.2f}")
st.info(f"Total Invested: ₹{inv:,.2f}")
st.info(f"Profit: ₹{corpus[-1] - inv:,.2f}")

st.subheader("📉 Growth Graph")
st.line_chart(df[["Invested", "Corpus"]])

st.subheader("📘 SIP Table")
st.dataframe(df)
