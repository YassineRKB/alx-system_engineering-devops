#!/usr/bin/python3
"""subriddit number of subsribers if subreddit is real"""
import requests


def number_of_subscribers(subreddit):
    """subriddit number of subsribers if subreddit is real"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'hey?'})
    req = requests.get(
        url,
        headers=headers
        ).json()
    count = req.get(
        'data',
        {}
        ).get('subscribers')
    if not count:
        return 0
    return count
