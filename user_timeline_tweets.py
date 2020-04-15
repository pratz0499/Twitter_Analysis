from tweepy import API
from tweepy import OAuthHandler
import twitter_credentials
import pandas as pd


class TwitterClient():
    def __init__(self):
        self.auth=TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client=API(self.auth)

    def get_user_tweets(self):
      mentions = self.twitter_client.mentions_timeline()
      users_details = [[mention.user.name,mention.user.screen_name,mention.text] for mention in mentions]
      tweet_text=pd.DataFrame(data=users_details,columns=["User_Name","User_Screen_Name","Tweets"])
      tweet_text.to_csv('mentions.csv')
      
      
class TwitterAuthenticator():
    def authenticate_twitter_app(self):
        auth=OAuthHandler(twitter_credentials.CONSUMER_KEY,twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN,twitter_credentials.ACCESS_TOKEN_SECRET)
        
        return auth
    
    
if __name__=="__main__":
    
    twitter_clients=TwitterClient()
    twitter_clients.get_user_tweets()