from twython import Twython, TwythonError
from twython import TwythonStreamer
from time import sleep
import random

APP_KEY='ymW03UtUFjIJrV1UN5QtP7KAt'
APP_SECRET='d8Q0Z4fbCuN3oOMy0aLpwSM4OOyGWqHVAXSa1cZxDXu6qi7CXh'
OAUTH_TOKEN='235318225-1cK0fhJes1JSQq5BkjGxLzC8Va2PKUxWzGw0E46H'
OAUTH_TOKEN_SECRET='GA8vNDmH9bxzG7C4vWoIu5KVWfZEzST4L4ZXZLZKSeH9p'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

while True:
    TweetMessage = "I love dogs"
    TweetPhoto = '/Users/Emily Hodder/Desktop/LEAPCodemakers2018/twitterbot/Images/dog.jfif'

    print(TweetMessage)
    print(TweetPhoto)

    photo = open(TweetPhoto,'rb')

    response = twitter.upload_media(media=photo)
    twitter.update_status(status=TweetMessage, media_ids=[response['media_id']])

    sleep(10)







