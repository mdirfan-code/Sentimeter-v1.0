from secrets import choice
import tweepy
import re
import praw


def clean_tweet(tweet):
    tweet = re.sub(r"@[A-Za-z0-9_]+", ' ', tweet)
    # Delete URL links
    tweet = re.sub(r"https?://[A-Za-z0-9./]+", ' ', tweet)
    # Just keep letters and important punctuation
    tweet = re.sub(r"[^a-zA-Z0-9.!?']", ' ', tweet)
    # Remove additional spaces
    tweet = re.sub(r" +", ' ', tweet)
    return tweet

def twitter_data(choice):
      # Access token to 
      access_token = "1340205660038778880-YA155aB955F6JaOLqhHBlFyb9YuDT2"
      access_token_secret = "bF014y4ICARPdKaW6C8lC4MFu8xoHzItScvtTJJdv1wo4"

      api_key = "79bgNhhOQZ0ZK5zZng1EvXtqA"
      api_key_secret = "xhxvVUL4qDbpOgl9XPo2OmGgNZWPrboscvnlMHvtOxyzAFAe6D"

      auth = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_key_secret)
      auth.set_access_token(access_token, access_token_secret)

      api = tweepy.API(auth)

      # choice = input("Enter Hashtag: ")
      

      tweets = tweepy.Cursor(api.search_tweets,q=choice).items(50)
      # print(type(tweets))
      ls = []
      ss = set()
      for tweet in tweets:
            # print(tweet)
            # print("---------------------------------------------------------------------------------\n")
            # print(tweet.created_at)
            
            if(not tweet.text.startswith("RT")):
                  # ls.append(tweet.text)
                  ls.append(clean_tweet(tweet.text))
            
      return ls
def reddit_data(post_id):
      user_agent = "Scraper/u/ashupandey31"
      reddit = praw.Reddit (
            client_id="79a-0hXv2mLU9PIojPcQAw",
            client_secret="TOGRmKo-Iqg_eNi00Gu5IyJQCs43xA",
            user_agent=user_agent
      )

      #headline = set()
      #for submission in reddit.subreddit('politics').hot(limit=10):
      submission = reddit.submission(post_id)
      submission.comments.replace_more(limit=None)
      ls = []
      ss = set()
      for comment in submission.comments.list():
            ls.append(clean_tweet(comment.body))
      
# print(data("forestfire"))
tt = "For every retweet this gets, Pedigree will donate one bowl of 1 dog food to dogs in need! 😊 #tweetforbowls https://pic.twitter.com/z4rmc2HsGT"
print(clean_tweet(tt))
      
      
