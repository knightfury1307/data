import pandas as pd
import tweepy 
import configparser


# read config file

config = configparser.ConfigParser()
config.read('config.ini')

API_KEY             = config['twitter']['API_KEY']
API_SECRET_KEY      = config['twitter']['API_SECRET_KEY']

ACCESS_TOKEN         = config['twitter']['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = config['twitter']['ACCESS_TOKEN_SECRET']

# authentication of twitter

auth = tweepy.OAuthHandler(API_KEY , API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN , ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

query = " -filter:links -PIC  -is:retweet"

public_tweets = api.search_tweets(q=query ,lang="en", count = 1000 )

columns = ['Time','User' , 'Tweet']
data =[]

for tweet in public_tweets:
    data.append([tweet.created_at , tweet.user.screen_name , tweet.text])

df = pd.DataFrame(data , columns=columns)
df.to_csv('tweets3.csv')

print(df)



