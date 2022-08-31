import pandas as pd
import tweepy 
import configparser


# read config file

config = configparser.ConfigParser()                
config.read('config.ini')

#stored secret key in a variable

API_KEY             = config['twitter']['API_KEY']
API_SECRET_KEY      = config['twitter']['API_SECRET_KEY']

ACCESS_TOKEN         = config['twitter']['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = config['twitter']['ACCESS_TOKEN_SECRET']

# authentication of twitter

auth = tweepy.OAuthHandler(API_KEY , API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN , ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

#query by which the tweets will be filtered

query = "#apex -filter:links -PIC  -is:retweet"                              

public_tweets = api.search_tweets(q=query ,lang="en", count = 1000 )

columns = ['Time','User' , 'Tweet']
data =[]                # make a empty list



for tweet in public_tweets:
    data.append([tweet.created_at , tweet.user.screen_name , tweet.text])

df = pd.DataFrame(data , columns=columns)                   #convert list to table using pandas
df.to_csv('tweets.csv')

#print(df)



