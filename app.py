import tweepy
import time;
import os;
from dotenv import load_dotenv
import requests;

load_dotenv()

auth = tweepy.OAuthHandler(os.environ.get('CONSUMER_KEY'), os.environ.get('CONSUMER_SECRET'))

auth.set_access_token(os.environ.get('ACCESS_TOKEN'), os.environ.get('ACCESS_SECRET'))

api = tweepy.API(auth, wait_on_rate_limit=True)

def random(): 
    try: 
        response = requests.get("https://quote-garden.herokuapp.com/api/v3/quotes/random")
        if response.status_code == 200:
            json = response.json()
            data = json['data']
            #adding tweet
            api.update_status(status=data[0]['quoteText'])
            print("Tweeted")
        
        else:
            print("Eh, there was an error while posting the tweet")
    
    except: 
        print("Eh, There was an exception while running the tweet");

random()


#Code for 1st tweet
# api.update_status(status="Was just bought to life. Still figuring this life thing out. ")

# print("tweeted")

#Search query parameters/
for tweet in api.search_tweets(q="cats", lang="en", count=10):   
    try:
        print("Tweet liked")
        #like tweet
        tweet.favorite()
        #retweeting
        tweet.retweet()
        print("")
        time.sleep(10)
    except tweepy.errors.TweepError as e:
        print("Tweet failed")
    except StopIteration:
        break;



