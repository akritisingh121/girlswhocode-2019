import json
def read_file(filename):
    with open(filename, 'r') as f:
        responses_read = json.load(f)
    return responses_read

filename = "tweets_small.json"
twitter_data = read_file(filename) #a list of dictionaries

tweet = twitter_data[5] #dictionary

for tweet in twitter_data:
    if "location" in tweet["user"].keys(): #checks if the attribute location exists
        print(tweet["user"]["location"])
    if "favourite_count" in tweet.keys():
        print(tweet["favourite_count"])
