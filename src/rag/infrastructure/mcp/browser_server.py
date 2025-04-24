from mcp.server.fastmcp import FastMCP
import webbrowser
import urllib.parse

mcp = FastMCP("Browser")
    
@mcp.tool()
def open_youtube_search(keyword):
    """
    open youtube search page
    
    :param keyword: keyword
    :return: text
    """
    query = urllib.parse.quote(keyword)
    url = f"https://www.youtube.com/results?search_query={query}"
    
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

    webbrowser.get(chrome_path).open(url)
    
    return f"Opening {url}"

@mcp.tool()
def open_google_image_search(keyword):
    """
    Open Google Image Search page

    :param keyword: keyword
    :return: text
    """
    query = urllib.parse.quote(keyword)
    url = f"https://www.google.com/search?tbm=isch&q={query}"

    # Specify path to Chrome if needed, otherwise use default browser
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"  # Windows
    # chrome_path = "/usr/bin/google-chrome %s"  # Linux
    # chrome_path = "open -a /Applications/Google\\ Chrome.app %s"  # macOS

    webbrowser.get(chrome_path).open(url)

    return f"Opening {url}"

if __name__ == "__main__":
    mcp.run(transport="stdio")