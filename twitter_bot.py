import tweepy
import time
import datetime
import os
from os import environ

now = datetime.datetime.now()

print('This is a twitter bot')

CONSUMER_KEY = environ['']
CONSUMER_SECRET = environ['xx2A9SAuvuJ38yBjcJB5IcxiSjWkFOm9PdnjJ95TcbkAZXEVKy']
ACCESS_KEY = environ['2615856414-nGxvEhvwQNmbUNxQJqIcEc6fjtAPVdpYzHHH5wi']
ACCESS_SECRET = environ['vVjSTxrVnMxtCT5AsnfGyv4iyUHQHsrgWGr5W35e3Fly1']


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id,file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

FILE_NAME_FAV = 'last_fav_tweet_id.txt'

def fav_tweet():
    print('Retrieving tweets...')
    last_seen_id = retrieve_last_seen_id(FILE_NAME_FAV)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode = 'extended')
    for mention in reversed(mentions):
        if not mention:
            return
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_fav_tweet = mention.id
        store_last_seen_id(last_fav_tweet,FILE_NAME_FAV)
        print('found @nog_nuus', flush = True)
        print('fav-ing and retweeting tweet...', flush = True)
        api.create_favorite(mention.id)
        api.retweet(mention.id)

while True:
    fav_tweet()
    time.sleep(15)
