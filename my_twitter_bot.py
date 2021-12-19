import os #for secrets
import tweepy
from time import sleep


CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_KEY = os.environ['ACCESS_KEY']
ACCESS_SECRET = os.environ['ACCESS_SECRET']



auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True) # https://stackoverflow.com/questions/41786569/twitter-error-code-429-with-tweepy
#https://stackoverflow.com/questions/58844898/how-to-follow-someone-on-twitter-using-tweepy-python

for tweet in tweepy.Cursor(api.search, q=('web3 OR token OR blockchain'), lang='en').items(400):
    try:
        # Add \n escape character to print() to organize tweets
        print('\nTweet by: @' + tweet.user.screen_name)

        # Retweet tweets as they are found
        tweet.retweet()
        print('Retweeted the tweet')

        sleep(5)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
