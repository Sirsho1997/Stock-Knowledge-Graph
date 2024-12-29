"""
This script downloads Open/High/Close/Low data from Yahoo Finance
"""
import yfinance as yf
import pandas as pd
import json
from datetime import datetime, timedelta
import os
def get_ohlc_data(ticker):
  """
  Fetches 1-day OHLC data for the given ticker using yfinance.

  Args:
    ticker: The stock ticker symbol.

  Returns:
    A pandas DataFrame containing the OHLC data.
  """
  try:
    today = datetime.today()
    last_month = today - timedelta(days=60)

    data = yf.download(ticker, start=last_month, end=today)
    return data[['Open', 'High', 'Low', 'Close']]
  except Exception as e:
    print(f"Error fetching data for {ticker}: {e}")
    return pd.DataFrame()


def main_run():
  #Fetch the list of Symbols/Tickers
  with open('scraped_data/ticker_name_dict.json', 'r') as f:
    data = json.load(f)

  tickers = data.get("Ticker", [])

  os.makedirs('stock_price_data', exist_ok=True)
  for ticker in tickers:
    # Loop through each ticker and fetch the Open/Close/High/Low data
    # Remove leading/trailing spaces from ticker name
    ticker = ticker.strip()

    # Fetch the Open/Close/High/Low data
    ohlc_df = get_ohlc_data(ticker)

    if len(ohlc_df) == 0:
      print(f"OHLC Data for {ticker} does not exist")
    else:

      # Save the price data
      ohlc_df.reset_index(inplace=True)
      ohlc_df.to_csv(f"stock_price_data/price_symbol_{ticker}.csv")


if __name__ == "__main__":
  main_run()
