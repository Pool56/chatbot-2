import requests
import os

DATAFORSEO_API = os.getenv("DATAFORSEO_API")

def get_keywords(keyword):

    url = "https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live"

    payload = [{
        "keywords":[keyword],
        "location_name":"United States",
        "language_name":"English"
    }]

    response = requests.post(url, json=payload, auth=(DATAFORSEO_API,""))

    data = response.json()

    keywords = []

    for item in data["tasks"][0]["result"]:
        keywords.append(item["keyword"])

    return keywords


if __name__ == "__main__":
    print(get_keywords("AI automation"))
