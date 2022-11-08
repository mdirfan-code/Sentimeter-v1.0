import praw

user_agent = "Scraper/u/ashupandey31"
reddit = praw.Reddit (
      client_id="79a-0hXv2mLU9PIojPcQAw",
      client_secret="TOGRmKo-Iqg_eNi00Gu5IyJQCs43xA",
      user_agent=user_agent
)

#headline = set()
#for submission in reddit.subreddit('politics').hot(limit=10):

submission = reddit.submission("yoqmmg")

submission.comments.replace_more(limit=None)
for comment in submission.comments.list():
      print("\n")
      print(comment.body)