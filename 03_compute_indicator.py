"""
This script generates indicator data on the Symbol/tickers  Open/High/Close/Low prices
"""
import os
import pandas as pd
import talib
import os

def compute_indicators(input_dir, output_dir):
    """
    Reads OHLC data from CSV files, computes SAR, RSI, and SMA using TA-Lib, and saves the results.

    Args:
        input_dir (str): Directory containing the input CSV files.
        output_dir (str): Directory to save the computed data.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # List all CSV files in the input directory
    csv_files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]

    for file in csv_files:
        try:
            # Read the data from CSV
            file_path = os.path.join(input_dir, file)

            # Read the 'Open', 'High', 'Low', 'Close' price
            df = pd.read_csv(file_path)
            df = df[['Date', 'Open', 'High', 'Low', 'Close']]

            # Compute indicators
            df['SAR'] = talib.SAR(df['High'], df['Low'], acceleration=0.02, maximum=0.2)
            df['RSI'] = talib.RSI(df['Close'], timeperiod=14)
            df['SMA'] = talib.SMA(df['Close'], timeperiod=14)

            # Select only last 5 days data and indicators value
            df = df[['Date', 'SAR', 'RSI', 'SMA']]
            df = df.tail(5)

            output_file = os.path.join(output_dir, file)
            df.to_csv(output_file, index=False)
            print(f"Processed and saved: {file}")

        except Exception as e:
            print(f"Error processing {file}: {e}")

def main_run():
    input_directory = 'stock_price_data'  # Directory containing OHLC data CSVs
    output_directory = 'stock_indicator_data'  # Directory to save computed data

    os.makedirs('stock_indicator_data', exist_ok=True)
    compute_indicators(input_directory, output_directory)

if __name__ == "__main__":
    main_run()
