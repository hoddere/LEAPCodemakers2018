#We need to import the premade packages that allow us to commuicate with the twitter API
from twython import Twython, TwythonError
from twython import TwythonStreamer

#importing this allows us to get random numbers
import random

#Importing this allows us to pause the code for a specified amount of time
#Similar to the delay() command we used in Arduino
from time import sleep

#We must define these variables using the personalized strings
#for the twitter account you wish to tweet from
APP_KEY='**************'
APP_SECRET='********************'
OAUTH_TOKEN='*********************'
OAUTH_TOKEN_SECRET='*****************************'

#Defines the twitter account using the Twython 
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    
#Define the text of your tweet
TweetMessage = 'Canada'
#Define the path to the photo you want to tweet
TweetPhoto = '/Users/Emily/Desktop/canada_flag.jpg'

#Open the photo
photo = open(TweetPhoto,'rb')

#Upload the photo to twitter
response = twitter.upload_media(media=photo)
#Attach the photo and the message to a tweet, and send the tweet
twitter.update_status(status=TweetMessage, media_ids=[response['media_id']])


"""
Some useful commands:

sleep(10) #Sleeps the program for 10 seconds
RandomNumber = random.randint(1,7) #Gets a random number from 1 to 7

"""

#Once you finish you can try experimenting with the search function
def searchTwitter():
    try:
        search_results = twitter.search(q='someones@', count=50)
    except TwythonError as e:
        print(e)

    for tweet in search_results['statuses']:
        print('Tweet from @%s Date: %s' % (tweet['user']['screen_name'].encode('utf-8'),tweet['created_at']))
        print (tweet['text'].encode('utf-8'), '\n')

