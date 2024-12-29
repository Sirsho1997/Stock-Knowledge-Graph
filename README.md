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

 Parsed the dictionaries and generated the pairwise relationship into a json object using [04_generate_relationship.py](https://github.com/Sirsho1997/Stock-Knowledge-Graph/blob/main/04_generate_relationship.py) and then generated a networkxx graph object based on the relationship using [05_generate_knowledge_graph.py](https://github.com/Sirsho1997/Stock-Knowledge-Graph/blob/main/05_generate_knowledge_graph.py). 

 Below is a screenshot of the relationship <br /> <br />
 <img width="626" alt="image" src="https://github.com/user-attachments/assets/c2f4ebf8-1de2-44ad-b61e-a302080078f0" />

 At the very end [06_visualizing_knowledge_graph.py](https://github.com/Sirsho1997/Stock-Knowledge-Graph/blob/main/06_visualizing_knowledge_graph.py) visualized the entire graph comprising of **1163 nodes** and **1166 edges** representing relationships between companies within each sector along with technical indicator analysis on price of company stock.

The entire graph can be viewed inside the HTML file [07_graph_data_pyvis.html](https://github.com/Sirsho1997/Stock-Knowledge-Graph/blob/main/07_graph_data_pyvis.html) generated by the [06_visualizing_knowledge_graph.py](https://github.com/Sirsho1997/Stock-Knowledge-Graph/blob/main/06_visualizing_knowledge_graph.py).
 

     

### **Application:**
 * Portfolio management for users based on their preferred sectors/stocks
 * Establishing pairwise relationships between sectors/ stocks that can help in grouping sectors to reduce investment risk


