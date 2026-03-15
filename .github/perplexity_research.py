import requests
import os

PERPLEXITY_API = os.getenv("PERPLEXITY_API")

def research_topic(topic):

    url = "https://api.perplexity.ai/chat/completions"

    payload = {
        "model": "pplx-70b-online",
        "messages": [
            {
                "role": "user",
                "content": f"Research the topic: {topic} and provide key insights"
            }
        ]
    }

    headers = {
        "Authorization": f"Bearer {PERPLEXITY_API}",
        "Content-Type": "application/json"
    }

    r = requests.post(url, json=payload, headers=headers)

    return r.json()["choices"][0]["message"]["content"]
