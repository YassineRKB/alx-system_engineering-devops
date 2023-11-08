#!/usr/bin/python3
"""function recurse """

import requests


def recurse(subreddit, hot_list=[], after="tmp"):
    """ recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit. If no
    results are found for the given subreddit, the function should return
    None."""
    if subreddit is None:
        return None
    url = f"http://www.reddit.com/r/{subreddit}/hot.json"
    user_agent = {'User-Agent': 'alx project test api token 54as8dw81aw84'}
    res = requests.get(
        url,
        params={"after": after},
        headers=user_agent,
        )
    if res.status_code == 200:
        after = res.json().get("data").get("after")
        if not after:
            return hot_list
        hot_list.extend(
            [post["data"]["title"] for post in res.json()["data"]["children"]]
            )
        return recurse(subreddit, hot_list, after)
