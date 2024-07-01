import praw
import requests
import json
import time

credentials = 'client_secrets.json'
 
with open(credentials) as f:
    creds = json.load(f)

# Authenticate to Reddit
reddit = praw.Reddit(client_id=creds['client_id'],
                     client_secret=creds['client_secret'],
                     user_agent=creds['user_agent'],
                     redirect_uri=creds['redirect_uri'],
                     refresh_token=creds['refresh_token'])

print('Logged in\n', reddit)

try:
    print(reddit.user.me())
except Exception as e:
    print(e)
# Define a subreddit to monitor
subreddit = reddit.subreddit("LiverpoolFC")
print(subreddit, "subreddit created")

for comment in subreddit.comments(limit=5):
    print(f"{comment.body}\n")
    if 'Gordon' in comment.body:  # Check if the comment contains 'darwin'
        comment.reply('Hello! Gordon can become GOAT under SLOT')  # Reply to the comment
        print('Replied to comment')
        time.sleep(20)  # Sleep for 10 seconds to avoid hitting Reddit’s API too frequently
