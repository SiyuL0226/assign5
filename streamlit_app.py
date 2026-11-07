import streamlit as st
import yfinance as yf
import pandas as pd

# Define ticker and monthly risk-free rate
ticker = "MSFT"
rf_monthly = 0.0025

# Download 5 years of monthly Microsoft stock data
data = yf.download(ticker, period="5y", interval="1mo")

if not data.empty:

    # Get closing prices
    close_prices = data["Close"][ticker]

    # Calculate monthly returns
    monthly_returns = close_prices.pct_change().dropna()

    # Calculate excess returns
    excess_returns = monthly_returns - rf_monthly

    # Average excess return
    mean_excess_return = excess_returns.mean()

    # Standard deviation of monthly returns
    std_dev_return = monthly_returns.std()

    # Calculate monthly Sharpe Ratio
    monthly_sharpe_ratio = mean_excess_return / std_dev_return

    # Display result
    st.metric(
        label="Microsoft Monthly Sharpe Ratio",
        value=f"{monthly_sharpe_ratio:.3f}"
    )

else:
    st.error("No data found for MSFT.")
