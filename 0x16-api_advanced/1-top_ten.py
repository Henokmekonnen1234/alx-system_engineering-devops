#!/usr/bin/python3
"""
Module 1-top_ten.py

This function will print top ten hot posts
"""

from requests import get


def top_ten(subreddit):
    """this function will print top ten hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    header = {"UserAgent": "CustomUserAgent"}
    try:
        with get(url, headers=header) as response:
            if response.status_code == 200:
                for data in response.json()["data"]["children"]:
                    print(data["data"]["title"])
            else:
                pass
    except Exception as e:
        pass
