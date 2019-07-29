import json
import numpy as np

def read_file(filename):
    with open(filename, 'r') as f:
        responses_read = json.load(f)
    return responses_read

filename = "tweets_small.json"
twitter_data = read_file(filename) #twitter_data is a list of dictionaries


#prints out the number of retweets and the number of hashtags that a tweet had.
def print_retweet_hashtag_info():
	for tweet in twitter_data[:]: #iterate through all the tweets in our list of tweets
		if "retweeted_status" in tweet.keys() and "hashtags" in tweet.keys():
			print("This tweet has " + str(tweet["retweeted_status"]["retweet_count"]) + " retweets.")
			hashtags = tweet["hashtags"]
			print("This tweet has " + str(len(hashtags)) + " hashtags.")
			if len(hashtags) > 0:
				texts = []
				for hashtag in hashtags:
					texts.append(hashtag["text"])
				print("The hashtags are: " + str(texts))
			print("------------")


#prints out user statistics
def print_user_statistics():
	friend_counts = []
	follower_counts = []
	favourite_counts = []
	for tweet in twitter_data: #iterate through all the tweets in our list of tweets
		user = tweet["user"]
		if ("friends_count" in user.keys()):
			friend_counts.append(user["friends_count"])
		if ("followers_count" in user.keys()):
			follower_counts.append(user["followers_count"])
		if ("favourites_count" in user.keys()):
			favourite_counts.append(user["favourites_count"])

	print("FRIENDS")
	print("The average friend count of Twitter users in this dataset is: " + str(np.average(friend_counts)))
	print("The minimum friend count of Twitter users in this dataset is: " + str(min(friend_counts)))
	print("The maximum friend count of Twitter users in this dataset is: " + str(max(friend_counts)))

	print("-------------")

	print("FOLLOWERS")
	print("The average follower count of Twitter users in this dataset is: " + str(np.average(follower_counts)))
	print("The minimum follower count of Twitter users in this dataset is: " + str(min(follower_counts)))
	print("The maximum follower count of Twitter users in this dataset is: " + str(max(follower_counts)))

	print("-------------")

	print("FAVOURITES")
	print("The average favourites count of Twitter users in this dataset is: " + str(np.average(favourite_counts)))
	print("The minimum favourites count of Twitter users in this dataset is: " + str(min(favourite_counts)))
	print("The maximum favourites count of Twitter users in this dataset is: " + str(max(favourite_counts)))

print_user_statistics()
print_retweet_hashtag_info()