#!/usr/bin/python3
"""count_words module"""
import requests


def count_words(subreddit, word_list, hot_dict=None, after=""):
    """words count"""
    if subreddit is None:
        return None
    if hot_dict is None:
        hot_dict = {}
    url = "http://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    user_agent = {'User-Agent': 'alx project test api token 5KSODKW2bd24'}
    res = requests.get(url, params={"after": after}, headers=user_agent)
    if res.status_code == 200:
        after = res.json()["data"].get("after")
        if not after:
            sorted_dict = sorted(hot_dict.items(), key=lambda x: (-x[1], x[0]))
            for word, occurrence in sorted_dict:
                print(f"{word}: {occurrence}")
            return
        for post in res.json()["data"]["children"]:
            title = post["data"]["title"].lower()
            for word in word_list:
                word = word.lower()
                if word in title:
                    hot_dict[word] = hot_dict.get(word, 0) + 1
        return count_words(subreddit, word_list, hot_dict, after)
