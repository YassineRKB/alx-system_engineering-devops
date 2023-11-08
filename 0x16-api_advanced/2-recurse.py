#!/usr/bin/python3
"""function recurse """

import requests


def recurse(subreddit, hot_list=[], after=""):
    """ recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit. If no
    results are found for the given subreddit, the function should return
    None."""
    if subreddit is None:
        return None
    url = "http://www.reddit.com/r/{}/hot.json".format(subreddit)
    user_agent = {"User-Agent": "mama mia where is betty"}

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
