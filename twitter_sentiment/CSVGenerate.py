import tweepy
from textblob import TextBlob
import sys
import csv

if len(sys.argv) >= 2:
	topic = sys.argv[1]
else:
	print("By default topic is Cricket.")
	topic = "Cricket"

consumer_key= 'Your Key'
consumer_secret= 'Your Key'

access_token='Your Key'
access_token_secret='Your Key'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search(topic)

with open('sentiment.csv', 'w', newline='\n') as  f:

	writer = csv.DictWriter(f, fieldnames=['Tweet', 'Sentiment'])
	writer.writeheader()
	for tweet in public_tweets:
		text = tweet.text
		#Cleaning tweet
		cleanedtext = " ".join([word for word in text.split(" ") if len(word) > 0 and word[0] != "@" and word[0] == "." and word[0] != "#" and "http" not in word and word != "RT"])

		analysis = TextBlob(cleanedtext)

		sentiment = analysis.sentiment.polarity
		if sentiment >= 0:
			polarity = 'Positive'
		else:
			polarity = 'Negative'

		#print(cleanedtext, polarity)

		writer.writerow({'Tweet':text, 'Sentiment':polarity})