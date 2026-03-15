import requests
import os

WP_URL = os.getenv("WP_URL")
WP_USER = os.getenv("WP_USER")
WP_PASSWORD = os.getenv("WP_PASSWORD")

def publish_post(title,content):

    post = {
        "title": title,
        "content": content,
        "status": "publish"
    }

    requests.post(
        f"{WP_URL}/wp-json/wp/v2/posts",
        json=post,
        auth=(WP_USER,WP_PASSWORD)
    )
