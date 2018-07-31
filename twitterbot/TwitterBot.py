from twython import Twython, TwythonError
import random
from twython import TwythonStreamer
from time import sleep

APP_KEY='ymW03UtUFjIJrV1UN5QtP7KAt'
APP_SECRET='d8Q0Z4fbCuN3oOMy0aLpwSM4OOyGWqHVAXSa1cZxDXu6qi7CXh'
OAUTH_TOKEN='235318225-1cK0fhJes1JSQq5BkjGxLzC8Va2PKUxWzGw0E46H'
OAUTH_TOKEN_SECRET='GA8vNDmH9bxzG7C4vWoIu5KVWfZEzST4L4ZXZLZKSeH9p'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

for i in range(5):

    RandomNumber = random.randint(1,7)
    print(RandomNumber)
    
    if RandomNumber==1:
        TweetMessage = 'Canada'
        TweetPhoto = '/Users/Emily Hodder/Desktop/LEAPCodemakers2018/twitterbot/Images/can.jpg'

    elif RandomNumber==2:
        TweetMessage = 'United States'
        TweetPhoto = '/Users/Emily Hodder/Desktop/LEAPCodemakers2018/twitterbot/Images/usa.jpg'

    elif RandomNumber==3:
        TweetMessage = 'Italy'
        TweetPhoto = '/Users/Emily Hodder/Desktop/LEAPCodemakers2018/twitterbot/Images/italy.jpg'

    elif RandomNumber==4:
        TweetMessage = 'France'
        TweetPhoto ='/Users/Emily Hodder/Desktop/LEAPCodemakers2018/twitterbot/Images/french.jpg'

    elif RandomNumber==5:
        TweetMessage = 'Germany'
        TweetPhoto = '/Users/Emily Hodder/Desktop/LEAPCodemakers2018/twitterbot/Images/germ.jpg'

    elif RandomNumber==6:
        TweetMessage = 'United Kingdom'
        TweetPhoto ='/Users/Emily Hodder/Desktop/LEAPCodemakers2018/twitterbot/Images/uk.jpg'

    elif RandomNumber==7:
        TweetMessage = 'Mexico'
        TweetPhoto ='/Users/Emily Hodder/Desktop/LEAPCodemakers2018/twitterbot/Images/mex.jpg'

    print(TweetMessage)
    print(TweetPhoto)

    photo = open(TweetPhoto,'rb')

    response = twitter.upload_media(media=photo)
    twitter.update_status(status=TweetMessage, media_ids=[response['media_id']])
    sleep(10)


########### If more advanced students finish early below are some ither tweepy commands 
###########they can play around with adn if they want others they can search tweepys site
########### This stuff has to do with searching other user info

    
try:
    search_results = twitter.search(q='someones@', count=50)
except TwythonError as e:
    print(e)

for tweet in search_results['statuses']:
    print('Tweet from @%s Date: %s' % (tweet['user']['screen_name'].encode('utf-8'),tweet['created_at']))
    print (tweet['text'].encode('utf-8'), '\n')



class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print(data['text'].encode('utf-8'))
        # Want to disconnect after the first result?
        #self.disconnect()

    def on_error(self, status_code, data):
        print(status_code, data)


stream = MyStreamer(APP_KEY, APP_SECRET,
                    OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

stream.statuses.filter(track='twitter')
