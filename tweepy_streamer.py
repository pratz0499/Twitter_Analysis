import pandas as pd
from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import twitter_credentials



class TwitterClient():
    def __init__(self):
        self.auth=TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client=API(self.auth)
        
    def get_usernames(self, num_tweets,lst_hashtags):
        tweets=Cursor(self.twitter_client.search,q=lst_hashtags,lang='en').items(num_tweets)
        
        #for i in Cursor(self.twitter_client.search,q=lst_hashtags,lang='en').items(num_tweets):
            
            #print(i)

        users_details = [[tweet.user.name, tweet.user.screen_name,tweet.user.location,tweet.text] for tweet in tweets]
        tweet_text=pd.DataFrame(data=users_details,columns=["User_Name","User_Screen_Name","Location","Tweets"])
        tweet_text.to_csv('tweets.csv')
        return tweet_text


class TwitterAuthenticator():
    def authenticate_twitter_app(self):
        auth=OAuthHandler(twitter_credentials.CONSUMER_KEY,twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN,twitter_credentials.ACCESS_TOKEN_SECRET)
        
        return auth
        

class TwitterStreamer():
    
    def __init__(self):
        self.twitter_authnenticator=TwitterAuthenticator()
    def stream_tweets(self, fetched_tweets_filename, lst_hashtags):
        """
        This handles twitter authentication and the connection
        to the twitter API.
        """
        listener=TwitterListener(fetched_tweets_filename)
        
        auth =self.twitter_authenticator.authenticate_twitter_app()
              
        stream=Stream(auth,listener)
    
        stream.filter(track=lst_hashtags)

class TwitterListener(StreamListener):
    
    def __init__(self,fetched_tweets_filename):
        self.fetched_tweets_filename=fetched_tweets_filename
        
    def on_data(self,data):
        try:
            print(data)
            with open(self.fetched_tweets_filename,"a") as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data: %s" %str(e))
        return True
    
    def on_error(self,status):
        if status==420:
            return False
        print(status)

if __name__=="__main__":
    lst_hashtags = ["#india", "#corona","#italy","#mumbai"]
    fetched_tweets_filename="tweets.csv"
    twitter_client=TwitterClient()
    for i in lst_hashtags:
        print(twitter_client.get_usernames(100,i))
    
    #Twitter_Streamer=TwitterStreamer()
    #Twitter_Streamer.stream_tweets(fetched_tweets_filename, lst_hashtags) 
    
    
        