#!/usr/bin/python3
"""Recursive function that queries Reddit API and returns all hot articles."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively queries the Reddit API and returns a list of all hot titles.

    If the subreddit is invalid, returns None.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return None

    if after is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    params = {"limit": 100, "after": after}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )
        if response.status_code != 200:
            return None

        data = response.json().get("data", {})
        after = data.get("after")
        children = data.get("children", [])
        if not children and not hot_list:
            return None

        for child in children:
            hot_list.append(child.get("data", {}).get("title"))

        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    except Exception:
        return None
