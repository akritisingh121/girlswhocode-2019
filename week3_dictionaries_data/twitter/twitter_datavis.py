from textblob import TextBlob
import json
import matplotlib.pyplot as plt

def read_file(filename):
    with open(filename, 'r') as f:
        responses_read = json.load(f)
    return responses_read

filename = "tweets_small.json"
twitter_data = read_file(filename) #twitter_data is a list of dictionaries

polarity = []
subjectivity = []

for tweet in twitter_data:
	text = TextBlob(tweet["text"])
	polarity.append(text.sentiment.subjectivity)
	subjectivity.append(text.sentiment.polarity)

plt.hist(polarity)
plt.title("Polarity of Tweets")
plt.xlabel("Polarity")
plt.ylabel("Density")
plt.show()

plt.hist(subjectivity)
plt.title("Subjectivity of Tweets")
plt.xlabel("Subjectivity")
plt.ylabel("Density")
plt.show()

plt.scatter(polarity, subjectivity)
plt.show()