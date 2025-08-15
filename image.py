import requests

FREEPIK_API_KEY = "FPSXa2beda86ec74036db6ba219f472b53a9"

def search_freepik_images(query, page=1):
    url = f"https://api.freepik.com/v1/resources"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {FREEPIK_API_KEY}"
    }
    params = {
        "q": query,
        "page": page,
        "limit": 10,
        "type": "photo"  # Options: photo, vector, psd, icon
    }

    res = requests.get(url, headers=headers, params=params)
    if res.ok:
        return [item["url"] for item in res.json()["data"]]
    else:
        return f"ERROR {res.status_code}: {res.text}"
