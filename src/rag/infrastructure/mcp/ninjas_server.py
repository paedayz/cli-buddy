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

if __name__ == "__main__":
    mcp.run(transport="stdio")