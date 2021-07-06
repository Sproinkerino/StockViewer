import pandas as pd
import praw
from datetime import datetime, timedelta
import time
date = '2021-06-29'

dt = datetime.strptime(date, '%Y-%m-%d').strftime('%B %d, %Y')
r = praw.Reddit(client_secret="uA3qH6Hlo3Uw3uHTtQ16sPYTkZg",
                client_id="ScDb4FtT9SJn0g",
                user_agent="Sproinkerino", )



subs =  r.subreddit("wallstreetbets").search("Daily Discussion Thread for "+ dt)
sub = subs.next()
sub.comments.replace_more()
sub

def print_text(text, level):

    print("{}%(body)s \n\n".format(level * '-') % (text))
    # if level == 0:
        # print("== On %(created)s ==\n\n" % (text))
def check_reply(comment, level):

    replies = comment.replies.list()
    if len(replies) == 0:
        return None
    else:
        for comm in replies:
            print_text(get_text(comm), level)
            check_reply(comm, level + 1)

def get_text(comment):
    # if comment.__class__ == praw.models.reddit.more.MoreComments:
    #     pass
    text = {

        'body': comment.body,
        'created': datetime_from_utc_to_local(comment.created_utc)
    }
    return text

def datetime_from_utc_to_local(utc_datetime):
    now_timestamp = time.time()
    dt= (datetime.utcfromtimestamp(utc_datetime))
    offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    return (dt + offset).strftime('%Y-%m-%d %H:%M:%S')

for comment in sub.comments.list():
    level = 0

    print_text(get_text(comment), level)

    check_reply(comment, level + 1)
    time.sleep(3)