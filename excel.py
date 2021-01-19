from openpyxl import Workbook
import datetime as dt
import tweepy
import numpy
from time import sleep

consumer_key = '8ZgghcwUoDm6gY8YYtlDSrzjH'
consumer_secret = 'RLSdYYGduGokDJ4nsKmhmumEpF99NNoqaQOrcLsxdCBWgYKk3k'
access_token_key = '1156170455147057152-6AC3AjpyEM1ixgRRulp04HrU04hU8L'
access_token_secret = 'jZLCfV7uQKeRU5CcHOgiFba26vF3Mm2Pxtx1RoznHa6rC'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)

Max = 10000

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "Phrases"
sheet["B1"] = "Depressed"

results = api.search(q="#Depressed -filter:retweets", maxResults=Max, count=Max, tweet_mode="extended")

index = 2

for tweet in results:
    sheet[f"A{index}"] = tweet.full_text
    sheet[f"B{index}"] = 1
    index = index + 1
    
results = api.search(q="#happy -filter:retweets", maxResults=Max, count=Max, tweet_mode="extended", include_rts = False)

for tweet in results:
    sheet[f"A{index}"] = tweet.full_text
    sheet[f"B{index}"] = 0
    index = index + 1
    
while True:
    try:
        workbook.save(filename="data/data.xlsx")
        break
    except:
        print("Currently busy trying again...")
        sleep(5)