import requests
import os

ANTHROPIC_KEY = os.getenv("ANTHROPIC_KEY")

def generate_article(keyword, research):

    url = "https://api.anthropic.com/v1/messages"

    prompt = f"""
Write a detailed SEO blog article.

Keyword:
{keyword}

Research Notes:
{research}
"""

    headers = {
        "x-api-key": ANTHROPIC_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }

    data = {
        "model": "claude-3-sonnet-20240229",
        "max_tokens": 2000,
        "messages": [{"role":"user","content":prompt}]
    }

    response = requests.post(url,json=data,headers=headers)

    return response.json()
