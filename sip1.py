import streamlit as st

st.set_page_config(page_title="SIP Calculator")
st.title("📈 SIP (Systematic Investment Plan) Calculator")

# Inputs
monthly_investment = st.number_input("Monthly Investment (₹)", min_value=0.0, value=1000.0)
years = st.number_input("Investment Duration (Years)", min_value=1, value=10)
rate = st.number_input("Expected Annual Return (%)", min_value=1.0, value=12.0)

months = int(years * 12)
monthly_rate = rate / 12 / 100

if st.button("Calculate SIP"):
    # SIP formula: FV = P * [ ((1+r)^n - 1 ) / r ] * (1+r)
    fv = monthly_investment * (((1 + monthly_rate) ** months - 1) / monthly_rate) * (1 + monthly_rate)
    
    invested_amount = monthly_investment * months
    returns = fv - invested_amount

    st.success(f"Future Value (Maturity Amount): ₹{fv:,.2f}")
    st.info(f"Total Invested: ₹{invested_amount:,.2f}")
    st.info(f"Wealth Gain: ₹{returns:,.2f}")
