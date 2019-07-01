from dotenv import load_dotenv
from os.path import join, dirname
import os
import tweepy

from flask import Flask, jsonify
app = Flask(__name__)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

user_name = 'yukinagae'  # TODO: dummy user


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/tweets")
def tweets():

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    timelines = api.user_timeline(user_name)

    urls = []

    for status in timelines[:100]:
        if status.retweeted:
            # TODO: this way of getting urls is not perfect
            # It misses some of the urls for some reasons.
            # maybe:
            # - `retweeted_status.entities['urls']`
            # as well.
            for url in status.entities['urls']:
                # print(f"{status.text[:20]}:{status.retweeted}")
                urls.append(url['expanded_url'])
                # print(url['expanded_url'])
    return jsonify(urls)
