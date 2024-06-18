#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit
"""
import requests
from collections import Counter


def count_words(subreddit, word_list, after=1, count=Counter()):
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
        for item in val:
            count.update(item['data']['title'].lower().split())
        after = r.json()['data']['after']
        if after is None:
            dic = {}
            for item in word_list:
                dic[item.lower()] = count[item.lower()]
            for x, y in sorted(dic.items(), key=lambda x: x[1], reverse=True):
                if y != 0:
                    print("{}: {}".format(x, y))
            return
        else:
            count_words(subreddit, word_list, after, count)
    except:
        pass
