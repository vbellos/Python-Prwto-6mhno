#!/usr/bin/python
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys

CONSUMER_KEY = 'LtGLFj52w0Eru69L4cBehcd86'
CONSUMER_SECRET = '6Fh66dUKcXNmMG79QvJaMzpxJEE7PX8tEwxDaLnY96okHyGIwS'
ACCESS_TOKEN = '1715778643-5nrkST70qnHvK7x5v15l2nhG1aOKDe1XvCsnKaW'
ACCESS_TOKEN_SECRET = '1h8zlwYtbkOsDpLCaTSrOvFSQMOFBQ6cBPm21aeLI8fwc'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
auth_api = API(auth)

def info(target):
	item = auth_api.get_user(target)
	print("name: " , item.name)
	print("followers: " , item.followers_count)
	print("\n")
	return item.followers_count

user1=raw_input("Dwse onoma xrhsth 1: \n")
user2=raw_input("Dwse onoma xrhsth 2: \n")


f1=info(user1)
f2=info(user2)

raw_input('Press enter to continue: ')

tweets1=auth_api.user_timeline(screen_name = user1,count=10,include_rts = False,tweet_mode = 'extended')
tweets2=auth_api.user_timeline(screen_name = user2,count=10,include_rts = False,tweet_mode = 'extended')

w1 = 0
print(user1)
for info in tweets1[:10]:
     print("ID: {}".format(info.id))
     print(info.created_at)
     print(info.full_text)
     print("\n")
     w1 = w1 + len(info.full_text)

print("synolikes lekseis",w1)

print(user2)
w2=0
for info in tweets2[:10]:
     print("ID: {}".format(info.id))
     print(info.created_at)
     print(info.full_text)
     print("\n")
     w2 = w2 + len(info.full_text)

print("synolikes lekseis",w2)    
     
raw_input('Press enter to continue: ')     

p1=w1*f1
p2=w2*f2

if p1>p2:
	print (user1,"exei megalytero ginomeno followers x lekseis")
else:
	print (user2,"exei megalytero ginomeno followers x lekseis")	
