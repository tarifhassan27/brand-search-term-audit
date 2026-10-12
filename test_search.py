import os
import requests

API_KEY = os.environ.get("YOUTUBE_API_KEY")
QUERY   = "dove"
MAX_RESULTS = 15

url = "https://www.googleapis.com/youtube/v3/search"
params = {
    "part":          "snippet",
    "q":             QUERY,
    "type":          "video",
    "videoDuration": "short",
    "maxResults":    MAX_RESULTS,
    "key":           API_KEY,
}

response = requests.get(url, params=params)
data = response.json()

print(f"Status: {response.status_code}")
print(f"Results returned: {len(data.get('items', []))}")
print()

for i, item in enumerate(data.get("items", []), 1):
    title   = item["snippet"]["title"]
    channel = item["snippet"]["channelTitle"]
    print(f"{i:>2}. [{channel}]  {title}")