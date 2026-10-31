#!/usr/bin/python3
"""Module that queries the Reddit API to get subreddit subscribers."""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers for a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; ALU-API-Advanced/1.0)"
    }

    response = requests.get(
        url,
        headers=headers,
        allow_redirects=False
    )

    if response.status_code != 200:
        return 0

    data = response.json().get("data")

    if data is None:
        return 0

    return data.get("subscribers", 0)
