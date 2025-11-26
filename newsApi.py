import requests

def getNews(q: str, sortBy: str, pageSize: int):
    params = {
       "q": q,
       "sortBy": sortBy,
       "pageSize": pageSize,
       "apiKey": "e783214a2657415aaf6a89f5cba2e69f"
    }
    response = requests.get("https://newsapi.org/v2/everything", params=params)
    return response.json()