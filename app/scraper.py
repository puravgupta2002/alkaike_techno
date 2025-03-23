import requests
from bs4 import BeautifulSoup

def fetch_tesla_news():
    bbc_url = "https://www.bbc.com/search?q=Tesla"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(bbc_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("h2")[:9]
    news_list = []

    for article in articles:
        title = article.text.strip()
        summary_div = article.find_next("div")
        summary = summary_div.text.strip() if summary_div else "Summary not available"
        news_list.append({"Title": title, "Summary": summary})

    return news_list
