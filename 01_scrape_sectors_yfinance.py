"""
This script scrapes Sector and Stock data from Yahoo Finance
"""


import requests
from bs4 import BeautifulSoup
import json
import os

def scrape_sector_names():
    """
    Scrapes sector names from the specified Yahoo Finance URL: https://finance.yahoo.com/sectors/

    Returns:
    A list of sector names.
    """

    url = 'https://finance.yahoo.com/sectors/'
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')
    elements = soup.find_all('td', class_='name yf-k3njn8')

    sector_names = [element.text for element in elements]
    return sector_names

def scrape_sector_symbols(sector_url):
  """
  Scrapes stock symbols from the specified sector URL.

  Args:
    sector_url: The URL of the sector page on Yahoo Finance.

  Returns:
    A list of stock symbols.
  """

  response = requests.get(sector_url)
  response.raise_for_status()  # Raise an exception for bad status codes

  soup = BeautifulSoup(response.content, 'html.parser')
  elements = soup.find_all('span', class_='symbol yf-1m808gl')

  stock_symbols = [element.text for element in elements]
  return stock_symbols

def main_run():
    sector_names = scrape_sector_names()

    sector_ticker_dict = {}
    ticker_names_combined = []


    for sector_name in sector_names:

        sector_name_url = sector_name.lower().split(' ')
        sector_name_url = '-'.join(sector_name_url)
        if sector_name_url == 'all-sectors':
            continue
        print(f"Sector: {sector_name_url}")

        sector_url = f"https://finance.yahoo.com/sectors/{sector_name_url}"
        stock_symbols = scrape_sector_symbols(sector_url)
        stock_symbols = stock_symbols[:5]
        sector_ticker_dict[sector_name] = stock_symbols
        ticker_names_combined.extend(stock_symbols)


        print(f"Stock Symbols: {stock_symbols}\n")

    ticker_names_dict = {}
    ticker_names_combined = list(set(ticker_names_combined))
    ticker_names_dict['Ticker'] = ticker_names_combined

    os.makedirs('scraped_data', exist_ok=True)
    with open('scraped_data/sector_ticker_dict.json', 'w') as outfile:
        json.dump(sector_ticker_dict, outfile, indent=4)

    with open('scraped_data/ticker_name_dict.json', 'w') as outfile:
        json.dump(ticker_names_dict, outfile, indent=4)

    pass

if __name__ == "__main__":
    main_run()

