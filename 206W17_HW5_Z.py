import unittest
import tweepy
import requests
import json
import twitter_info

## SI 206 - W17 - HW5
## COMMENT WITH: Scott Zabrowski
## Your section day/time: Friday 1:00pm - 2:00pm
## Any names of people you worked with on this assignment: N/A

######## 500 points total ########

## Write code that uses the tweepy library to search for tweets with a phrase of the user's choice (should use the Python input function), and prints out the Tweet text and the created_at value (note that this will be in GMT time) of the first THREE tweets with at least 1 blank line in between each of them, e.g.

## TEXT: I'm an awesome Python programmer.
## CREATED AT: Sat Feb 11 04:28:19 +0000 2017

## TEXT: Go blue!
## CREATED AT: Sun Feb 12 12::35:19 +0000 2017

## .. plus one more.

## You should cache all of the data from this exercise in a file, and submit the cache file along with your assignment. 

## So, for example, if you submit your assignment files, and you have already searched for tweets about "rock climbing", when we run your code, the code should use CACHED data, and should not need to make any new request to the Twitter API. 
## But if, for instance, you have never searched for "bicycles" before you submitted your final files, then if we enter "bicycles" when we run your code, it _should_ make a request to the Twitter API.

## The lecture notes and exercises from this week will be very helpful for this. 
## Because it is dependent on user input, there are no unit tests for this -- we will run your assignments in a batch to grade them!

## We've provided some starter code below, like what is in the class tweepy examples.

## **** For 50 points of extra credit, create another file called twitter_info.py that contains your consumer_key, consumer_secret, access_token, and access_token_secret, import that file here, and use the process we discuss in class to make that information secure! Do NOT add and commit that file to a public GitHub repository.
consumer_key = twitter_info.consumer_key
consumer_secret = twitter_info.consumer_secret
access_token = twitter_info.access_token
access_token_secret = twitter_info.access_token_secret
## **** If you choose not to do that, we strongly advise using authentication information for an 'extra' Twitter account you make just for this class, and not your personal account, because it's not ideal to share your authentication information for a real account that you use frequently.

## Get your secret values to authenticate to Twitter. You may replace each of these with variables rather than filling in the empty strings if you choose to do the secure way for 50 EC points
# consumer_key = "" 
# consumer_secret = ""
# access_token = ""
# access_token_secret = ""
## Set up your authentication to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser()) # Set up library to grab stuff from twitter with your authentication, and return it in a JSON-formatted way


## Write the rest of your code here!

cache = "tweepyHW5.json"
try:
	cache_file_obj = open(cache,'r')
	cache_contents = cache_file_obj.read()
	cache_d = json.loads(cache_contents)
except:
	cache_d = {}


public_tweets = api.home_timeline()
#print (type(public_tweets))

user = input("Type in what you want to search")
#user = "Michigan"
API = api.search(q = user,rpp = 1)

unique_id = "twitter_{}".format(user)
if unique_id in cache_d:
	search = cache_d[unique_id]
else:
	search = API
	cache_d[unique_id] = search
	f = open(cache,'w')
	f.write(json.dumps(API))
	f.close()

#print (len(search))
#print (search.keys())

list_tweets = search['statuses']
#print (list_tweets)

lst = []
lst1 = []

for tweet in list_tweets:
    lst.append(tweet['text'])
    lst1.append(tweet['created_at'])
    #print (tweet['text'])
    #print (tweet['created_at'])

# print (lst[:3])
# print (lst1[:3])
lst = lst[:3]
lst1 = lst1[:3]

for x in lst:
	print (x)
	z = lst.index(x)
	print (lst1[z])
	print ('\n')



#### Recommended order of tasks: ####
## 1. Set up the caching pattern start -- the dictionary and the try/except statement shown in class.
## 2. Write a function to get twitter data that works with the caching pattern, so it either gets new data or caches data, depending upon what the input to search for is. You can model this off the class exercise from Tuesday.
## 3. Invoke your function, save the return value in a variable, and explore the data you got back!
## 4. With what you learn from the data -- e.g. how exactly to find the text of each tweet in the big nested structure -- write code to print out content from 3 tweets, as shown above.


























