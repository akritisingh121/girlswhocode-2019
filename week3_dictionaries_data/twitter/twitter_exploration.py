from textblob import TextBlob
import json

def read_file(filename):
    with open(filename, 'r') as f:
        responses_read = json.load(f)
    return responses_read

filename = "tweets_small.json"
twitter_data = read_file(filename) #a list of dictionaries

tweet = twitter_data[5] #dictionary

polarityList = []
for tweet in twitter_data:
	tweetblob = TextBlob(tweet["text"])
	polarityList.append(tweetblob.polarity)

print(polarityList)