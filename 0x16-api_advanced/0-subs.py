#!/usr/bin/python3
"""
Module 0-subs.py

This module will requested data from Reddit API and it will return
data like number of subscriber
"""

from requests import get


def number_of_subscribers(subreddit):
    """Reddit API end point getting number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'CustomUserAgent'}
    try:
        with get(url, headers=headers) as response:
            if response.status_code == 200:
                data = response.json()
                return data["data"]["subscribers"]
            else:
                return 0
    except Exception as e:
        return 0
