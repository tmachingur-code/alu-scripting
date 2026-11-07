#!/usr/bin/python3
"""Recursive function that queries Reddit API and counts keyword frequency."""
import requests


def count_words(subreddit, word_list, after=None, raw_counts=None):
    """Recursively parses all hot titles and counts keywords."""
    if not subreddit or not isinstance(subreddit, str) or not word_list:
        return

    if raw_counts is None:
        raw_counts = {}

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
            return

        data = response.json().get("data", {})
        after = data.get("after")
        posts = data.get("children", [])

        normalized_targets = set(w.lower() for w in word_list)

        for post in posts:
            title = post.get("data", {}).get("title", "")
            for word in title.lower().split():
                if word in normalized_targets:
                    raw_counts[word] = raw_counts.get(word, 0) + 1

        if after is not None:
            return count_words(subreddit, word_list, after, raw_counts)

        multipliers = {}
        for w in word_list:
            w_low = w.lower()
            multipliers[w_low] = multipliers.get(w_low, 0) + 1

        final_counts = {}
        for w_low, count in raw_counts.items():
            if count > 0:
                final_counts[w_low] = count * multipliers.get(w_low, 1)

        sorted_results = sorted(
            final_counts.items(), key=lambda x: (-x[1], x[0])
        )

        for word, count in sorted_results:
            print("{}: {}".format(word, count))

    except Exception:
        returni
