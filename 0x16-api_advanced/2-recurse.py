#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=1):
    """ prints the titles of the first 10 hot posts listed"""
    if after is 1:
        r = requests.get('https://www.reddit.com/r/{}/hot.json'.
                         format(subreddit),
                         headers={'User-Agent': 'jack'},
                         allow_redirects=False)
    else:
        r = requests.get('https://www.reddit.com/r/{}/hot.json'.
                         format(subreddit),
                         headers={'User-Agent': 'jack'},
                         params={'after': after},
                         allow_redirects=False)
    try:
        val = r.json()['data']['children']
        hot_list += [x['data']['title'] for x in val]
        after = r.json()['data']['after']
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    except:
        return None
