# Project: Knowledge Graph from Stock Data

This project focuses on building a knowledge graph from stock data sourced from Yahoo Finance. 

**Key Features:**

* **Data Collection:**
  *   Scraped list of **sectors** and corresponding **tickers/symbols** grouped in the sector from [Yahoo Finance](https://finance.yahoo.com/) using the script [01_scrape_sectors_yfinance.py](https://github.com/Sirsho1997/Stock-Knowledge-Graph/blob/main/01_scrape_sectors_yfinance.py) within the following sectors:
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


* **Knowledge Graph Construction:**
    * Creates a graph representation of the relationships between companies within each sector.
    * Identifies potential correlations and dependencies among stocks.
    * May incorporate external data sources (e.g., news, economic indicators) to enrich the graph.

* **Analysis and Visualization:**
    * Utilizes graph algorithms for tasks such as:
        * Community detection (identifying clusters of closely related stocks)
        * Anomaly detection (finding unusual stock price movements)
        * Pathfinding (analyzing potential investment pathways)
    * Visualizes the knowledge graph using interactive tools (e.g., network diagrams).

**Potential Applications:**

* **Investment Portfolio Management:**
    * Optimize portfolio diversification by identifying sectors with low correlation.
    * Generate investment strategies based on predicted stock price movements.
* **Risk Assessment:**
    * Identify systemic risks within specific sectors.
    * Assess the impact of external events on stock prices.
* **Market Research:**
    * Gain insights into industry trends and competitive landscapes.
    * Discover new investment opportunities.

**Technologies Used:**

* **Data Sources:** Yahoo Finance API
* **Programming Languages:** Python (e.g., Pandas, NumPy, NetworkX)
* **Data Visualization:** Libraries like matplotlib, seaborn, or interactive JavaScript libraries

**Further Development:**

* Incorporate machine learning models for predictive analysis.
* Integrate real-time data streams for dynamic graph updates.
* Develop a user-friendly interface for interacting with the knowledge graph.

This README provides a general overview of the project. For more detailed information, please refer to the project documentation and source code.
