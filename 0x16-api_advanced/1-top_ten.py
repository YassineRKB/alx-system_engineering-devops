#!/usr/bin/python3
"""get top ten posts of a subreddit passed as argument"""
import requests


def top_ten(subreddit):
    """Print None if invalid or top ten titles for a valid subreddit"""
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'mom!'})
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    req = requests.get(
        url,
        params={"limit": 10},
        headers=headers
        ).json()
    posts = req.get(
        'data',
        {}
        ).get('children', [])
    if not posts:
        print(None)
    for title in posts:
        print(title.get('data').get('title'))
