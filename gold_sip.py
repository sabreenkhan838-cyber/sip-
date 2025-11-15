import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Page settings
st.set_page_config(page_title="Gold SIP Calculator", layout="wide")
st.title("🏆 Gold SIP Calculator with Growth Graph")

# ---- INPUTS ----
monthly_investment = st.number_input("📥 Monthly Investment (₹)", min_value=0.0, value=2000.0)
years = st.number_input("📅 Investment Duration (Years)", min_value=1, value=10)
expected_growth = st.number_input("📈 Expected Annual Gold Price Growth (%)", min_value=0.0, value=8.0)

months = int(years * 12)
monthly_rate = expected_growth / 12 / 100

# ---- SIMULATION ----
corpus = []
invested = []
current_value = 0
total_invested = 0

for i in range(months):
    total_invested += monthly_investment
    current_value = current_value * (1 + monthly_rate) + monthly_investment
    corpus.append(current_value)
    invested.append(total_invested)

df = pd.DataFrame({
    "Month": range(1, months + 1),
    "Invested (₹)": invested,
    "Corpus Value (₹)": corpus
})

# ---- RESULTS ----
st.subheader("📊 Results")
st.success(f"Projected Gold SIP Corpus: ₹{corpus[-1]:,.2f}")
st.info(f"Total Invested: ₹{total_invested:,.2f}")
st.info(f"Estimated Profit: ₹{corpus[-1] - total_invested:,.2f}")

# ---- GRAPH ----
st.subheader("📉 SIP Growth Chart")

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df["Month"], df["Corpus Value (₹)"], label="Corpus Value", linewidth=2)
ax.plot(df["Month"], df["Invested (₹)"], label="Total Invested", linestyle="--")
ax.set_xlabel("Months")
ax.set_ylabel("Amount (₹)")
ax.legend()
ax.grid(True)

st.pyplot(fig)

# ---- TABLE ----
st.subheader("📘 Detailed SIP Table")
st.dataframe(df.style.format({"Invested (₹)": "{:,.2f}", "Corpus Value (₹)": "{:,.2f}"}))

