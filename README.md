# Knowledge Graph from Stock Data

This project focuses on building a knowledge graph from stock data sourced from Yahoo Finance. 



### **Data Collection:**
 *   Scraped list of **sectors** and corresponding company **tickers/symbols** grouped in the sector from [Yahoo Finance](https://finance.yahoo.com/) using the script [01_scrape_sectors_yfinance.py](https://github.com/Sirsho1997/Stock-Knowledge-Graph/blob/main/01_scrape_sectors_yfinance.py) within the following sectors:
       * Technology
       * Financial Services
       * Consumer Cyclical
       * Healthcare
       * Communication Services
       * Industrials
       * Consumer Defensive
       * Energy
       * Real Estate
       * Basic Materials
       * Utilities
   *   Downloaded **Open**, **Close**, **High**, and **Low** **prices** for each of the tickers/symbols such as AAPL (Apple Inc), GOOG (Google LLC) within the list of sectors mentioned above using [02_download_price_data.py](https://github.com/Sirsho1997/Stock-Knowledge-Graph/blob/main/02_download_price_data.py)

   * Calculated **technical indicators** (described below) for the past 5 days for each **ticker/symbol** using [03_compute_indicator.py](https://github.com/Sirsho1997/Stock-Knowledge-Graph/blob/main/03_compute_indicator.py)
       *  **Parabolic SAR (Stop and Reverse):** Trend-following indicator that identifies potential reversals. 

       *  **Relative Strength Index (RSI):** Momentum oscillator that measures the magnitude of recent price changes to evaluate overbought/oversold conditions.
       *  **Simple Moving Average (SMA):** Calculates the average price of a security over a specific number of period. 


### **Knowledge Graph Construction:**
 Generated a graph comprising of **1163 nodes** and **1166 edges** representing relationships between companies within each sector along with technical indicator analysis on price of company stock.
     

### **Application:**
 * Portfolio management for users based on their preferred sectors/stocks
 * Establishing pairwise relationships between sectors/ stocks that can help in grouping sectors together to reduce investment risk


