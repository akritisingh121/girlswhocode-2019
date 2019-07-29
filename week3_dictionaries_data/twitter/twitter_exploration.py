import json

def read_file(filename):
    with open(filename, 'r') as f:
        responses_read = json.load(f)
    return responses_read

filename = "tweets_small.json"
twitter_data = read_file(filename) #twitter_data is a list of dictionaries

tweet = twitter_data[5] #tweet is a dictionary

for tweet in twitter_data: #iterate through all the tweets in our list of tweets
	for key, val in tweet.items(): #use this syntax to iterate over the keys and values in a dictionary
		print(key)
		print(val)
		print() #prints an empty line
	

#for each tweet, this prints the location of the user that
#posted it
for tweet in twitter_data:
	if "location" in tweet["user"].keys():
		print(tweet["user"]["location"])