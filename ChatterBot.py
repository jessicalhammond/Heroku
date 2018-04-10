# Dependencies
import numpy as np
import pandas as pd
import tweepy
import time
import json
from config import consumer_key, consumer_secret, access_token, access_token_secret


# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)


# Create Thank You Function
def ThankYou():

    # Twitter Credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Search for all tweets
    public_tweets = api.search(target_term, count=10, result_type="recent")

    # Loop through all tweets
    for tweet in public_tweets['statuses']:
        tweet_id = tweet['id']
        tweet_author = tweet['user']['screen_name']
        print(tweet_id)

        try:
            api.update_status("Gotta update them config files @%s! #omg" %
                             tweet_author,
                             in_reply_to_status_id=tweet_id)
            print("Success")
        except Exception:
            print("Already responded")

        print("Done for now, check again soon.")
        # Print message to signify complete cycle




# CODE GOES HERE