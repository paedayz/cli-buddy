from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
import os
import requests

load_dotenv()

NINIJAS_API_KEY = os.getenv('NINIJAS_API_KEY')

mcp = FastMCP("Ninjas API")

URL = 'https://api.api-ninjas.com'

@mcp.tool()
def get_calories_burned(activity):
    """
    get calories burned data
    
    :param activity: activity
    :return: calories
    """
    api_url = '{}/v1/caloriesburned?activity={}'.format(URL, activity)
    response = requests.get(api_url, headers={'X-Api-Key': NINIJAS_API_KEY})
    if response.status_code == requests.codes.ok:
        return response.text
    else:
        return f"Error: {response.text}"
    
    
@mcp.tool()
def get_random_quote():
    """
    get random quote
    
    :param None
    :return: quote
    """
    api_url = '{}/v1/quotes'.format(URL)
    response = requests.get(api_url, headers={'X-Api-Key': NINIJAS_API_KEY})
    if response.status_code == requests.codes.ok:
        return response.text
    else:
        return f"Error: {response.text}"

@mcp.tool()
def get_exchange_rate(from_currency, to_currency):
    """
    get exchange rate
    
    :param from_currency: from currency
    :param to_currency: to currency
    
    params example:
        from_currency = 'USD'
        to_currency = 'EUR'
        
    :return: exchange rate
    """
    api_url = '{}/v1/exchangerate?pair={}_{}'.format(URL, from_currency, to_currency)
    response = requests.get(api_url, headers={'X-Api-Key': NINIJAS_API_KEY})
    if response.status_code == requests.codes.ok:
        return response.text
    else:
        return f"Error: {response.text}"
    
    
@mcp.tool()
def get_bitcoin_price():
    """
    get bitcoin price
    
    :param None
    :return: price
    """
    api_url = '{}/v1/bitcoin'.format(URL)
    response = requests.get(api_url, headers={'X-Api-Key': NINIJAS_API_KEY})
    if response.status_code == requests.codes.ok:
        return response.text
    else:
        return f"Error: {response.text}"
    
    
@mcp.tool()
def get_stock_price(ticker):
    """
    get stock price
    
    :param ticker: ticker
    :return: price
    """
    api_url = '{}/v1/stock?ticker={}'.format(URL, ticker)
    response = requests.get(api_url, headers={'X-Api-Key': NINIJAS_API_KEY})
    if response.status_code == requests.codes.ok:
        return response.text
    else:
        return f"Error: {response.text}"

if __name__ == "__main__":
    mcp.run(transport="stdio")