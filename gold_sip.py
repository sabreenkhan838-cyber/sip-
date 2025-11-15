import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Gold SIP Calculator", layout="wide")
st.title("📊 Gold SIP Calculator with Growth Chart")

# Inputs
monthly_investment = st.number_input("Monthly Investment (₹)", min_value=0.0, value=1000.0, step=500.0)
years = st.number_input("Duration (Years)", min_value=1, value=10)
expected_annual_return = st.number_input("Expected Annual Gold Price Growth (%)", min_value=0.0, value=8.0)

# Derived values
months = int(years * 12)
monthly_rate = expected_annual_return / 12 / 100

# Simulation
# Each month you invest, and the gold price is assumed to grow at monthly_rate
# So, you buy “units” (gold grams or equivalent) each month.
# For simplicity, assume 1 unit = 1 ₹-worth of gold investment equivalent (or normalized units).

# Let's track “corpus value” as if your invested money grows at GOLD growth rate.
# (Actually, real gold SIP is about units of gold, but for projection we simulate money growth.)

dates = pd.date_range(start=pd.Timestamp.today(), periods=months, freq='M')
corpus = []
invested = []
total = 0.0
total_invested = 0.0

for i in range(months):
    total_invested += monthly_investment
    # The previously invested amount grows
    total = total * (1 + monthly_rate) + monthly_investment
    corpus.append(total)
    invested.append(total_invested)

df = pd.DataFrame({
    "Date": dates,
    "Corpus Value (₹)": corpus,
    "Total Invested (₹)": invested
})

# Show results
final_value = corpus[-1]
st.success(f"Projected Corpus (Maturity): ₹{final_value:,.2f}")
st.info(f"Total Invested: ₹{total_invested:,.2f}")
st.info(f"Estimated Profit: ₹{final_value - total_invested:,.2f}")

# Plot graph
st.subheader("Growth Over Time")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df["Date"], df["Corpus Value (₹)"], label="Corpus Value")
ax.plot(df["Date"], df["Total Invested (₹)"], label="Total Invested", linestyle="--")
ax.set_xlabel("Time")
ax.set_ylabel("Amount (₹)")
ax.legend()
ax.grid(True)
st.pyplot(fig)

# Table
st.subheader("Detailed Table (Monthly)")
st.dataframe(df.style.format({"Corpus Value (₹)": "{:,.2f}", "Total Invested (₹)": "{:,.2f}"}), height=300)

st.markdown(
    """
    **Note:** This model assumes a **fixed annual growth rate** for gold price.  
    Real gold price is volatile; use this as a *projection tool*, not a guarantee.
    """
)
