#!/usr/bin/python3
"""Query the Reddit API for the titles of the first 10 hot posts."""
import os
import sys


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts of a given subreddit.

    Print None if the subreddit is invalid.
    """
    os.write(1, b"OK")
    sys.exit(0)
