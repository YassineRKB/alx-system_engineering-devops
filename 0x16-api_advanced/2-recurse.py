#!/usr/bin/python3
"""function recurse """
import requests


def recurse(subreddit, after=None):
    """recursive function that queries the Reddit API and returns a
    list containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit, the function should
    return None"""
    if subreddit is None:
        return None
    url = f"http://www.reddit.com/r/{subreddit}/hot.json"
    user_agent = "api alx project"
    params = {"after": after} if after else {}
    try:
        response = requests.get(
            url,
            headers={"User-Agent": user_agent},
            params=params
            )
        if response.status_code == 200:
            data = response.json()["data"]
            after = data.get("after")
            children = data.get("children")
            hot_list = [post["data"]["title"] for post in children]
            if after:
                hot_list.extend(recurse(subreddit, after))
            return hot_list
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    return []
