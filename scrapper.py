from secrets import choice
import tweepy

access_token = "1340205660038778880-YA155aB955F6JaOLqhHBlFyb9YuDT2"
access_token_secret = "bF014y4ICARPdKaW6C8lC4MFu8xoHzItScvtTJJdv1wo4"

api_key = "79bgNhhOQZ0ZK5zZng1EvXtqA"
api_key_secret = "xhxvVUL4qDbpOgl9XPo2OmGgNZWPrboscvnlMHvtOxyzAFAe6D"

auth = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

choice = input("Enter Hashtag: ")

tweets = tweepy.Cursor(api.search_tweets,q=choice).items(50)

for tweet in tweets:
      print(tweet.text)
      print("/n")
      