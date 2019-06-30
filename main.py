import tweepy

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

user_name = 'yukinagae'  # TODO: dummy user

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

timelines = api.user_timeline(user_name)

for status in timelines[:20]:
    if status.retweeted:
        print(f"{status.text[:20]}:{status.retweeted}")
        # TODO: this way of getting urls is not perfect
        # It misses some of the urls for some reasons.
        # maybe:
        # - `retweeted_status.entities['urls']`
        # as well.
        for url in status.entities['urls']:
            print(url['expanded_url'])
