"""
This script generates the pairwise relationship between the stock/sector/indicator
"""
import json
import pandas as pd
import os
def create_stock_relationships(data_dir):
    """
    Creates a JSON file containing stock relationships based on sector and technical indicators.

    Args:
        data_dir: Directory containing CSV files with stock data.

    Returns:
        None
    """

    with open("scraped_data/sector_ticker_dict.json", "r") as f:
        sector_ticker_dict = json.load(f)

    relationships = {"Stock": {}}
    for sector, tickers in sector_ticker_dict.items():
        relationships["Stock"][sector] = {}
        for ticker in tickers:
            try:
                df = pd.read_csv(f"{data_dir}/price_symbol_{ticker.strip()}.csv")
                df.columns = ["Date", "SAR", "RSI", "SMA"]
                df = df.set_index("Date")

                stock_data = {}
                for i, row in df.iterrows():
                    day = f"Day {i}"
                    stock_data[day] = {
                        "RSI": row["RSI"],
                        "SMA": row["SMA"],
                        "SAR": row["SAR"]
                    }

                relationships["Stock"][sector][ticker.strip()] = stock_data

            except FileNotFoundError:
                print(f"Warning: File not found for {ticker}")

    os.makedirs('graph_data', exist_ok=True)
    with open("graph_data/stock_relationships.json", "w") as f:
        json.dump(relationships, f, indent=4)

    pass

if __name__ == "__main__":
    create_stock_relationships("stock_indicator_data")



