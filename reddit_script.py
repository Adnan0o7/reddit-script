import praw
import requests
import json
import time
import datetime

credentials = 'client_secrets.json'
 
with open(credentials) as f:
    creds = json.load(f)

# Authenticate to Reddit
reddit = praw.Reddit(client_id=creds['client_id'],
                     client_secret=creds['client_secret'],
                     user_agent=creds['user_agent'],
                     redirect_uri=creds['redirect_uri'],
                     refresh_token=creds['refresh_token'])
try:
    print(f"{reddit.user.me()} is logged in successfully ...")

    # Define a subreddit to monitor
    subreddit = reddit.subreddit("PrawScript")
    print("Using subreddit {subreddit}")
    
    print("Send private message to user ...")
    reddit.redditor('Adnan_Ansari').message(subject='Suggestion', message='Hey.. Test bot message')
    
    for message in reddit.inbox.sent():
        # message.delete()
        pass

    for comment in subreddit.comments(limit=25):
        if 'comment' in comment.body:
            print(f"User matched >>>>>>>> {comment.author}\n\n{comment.body}\n")
            interested_user = comment.author
            comment.reply("replied to comment")
            time.sleep(2)

except Exception as e:
    print(e)