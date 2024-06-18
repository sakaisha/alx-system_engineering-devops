#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts listed"""
    r = requests.get('https://www.reddit.com/r/{}/hot.json'.
                     format(subreddit),
                     headers={'User-Agent': 'jack'},
                     params={'limit': 10},
                     allow_redirects=False)
    try:
        val = r.json()['data']['children']
        for item in val:
            print(item['data']['title'])
    except:
        print ("None")
