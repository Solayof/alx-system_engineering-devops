#!/usr/bin/python3
"""
Contains a function that works with Reddit API
"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'solayof'}
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        res = res.json()
        subs = res.get('data').get('subscribers')
        return subs
    return 0
