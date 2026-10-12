import requests
import csv
import time

API_KEY = os.environ.get("YOUTUBE_API_KEY")

SEARCH_TERMS = [
    # Brand core
    "dove soap", "dove shampoo", "dove deodorant", "dove body wash",
    # Product specific
    "dove beauty bar", "dove dry shampoo", "dove moisturizer", "dove face wash",
    # Campaign
    "dove real beauty", "dove self esteem", "dove realbody", "dove care",
    # Misspellings
    "dov soap", "doove", "dove sop", "dove shampo",
    # Ambiguous
    "dove", "dove cameron", "dove bird", "dove chocolate",
]

URL = "https://www.googleapis.com/youtube/v3/search"

rows = []

for term in SEARCH_TERMS:
    print(f"Fetching: {term}")
    params = {
        "part":          "snippet",
        "q":             term,
        "type":          "video",
        "videoDuration": "short",
        "maxResults":    15,
        "key":           API_KEY,
    }
    response = requests.get(URL, params=params)
    data = response.json()

    items = data.get("items", [])
    print(f"  → {len(items)} results")

    for item in items:
        if item.get("id", {}).get("kind") != "youtube#video":
            continue
        rows.append({
            "search_term":   term,
            "video_id":      item["id"]["videoId"],
            "title":         item["snippet"]["title"],
            "channel":       item["snippet"]["channelTitle"],
            "published_at":  item["snippet"]["publishedAt"],
            "label":         "",
        })

    time.sleep(1)  # be polite to the API

# Save to CSV
output_file = "raw_results.csv"
with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["search_term","video_id","title","channel","published_at","label"])
    writer.writeheader()
    writer.writerows(rows)

print(f"\nDone. {len(rows)} rows saved to {output_file}")