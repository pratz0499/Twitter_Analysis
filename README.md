# Twitter Analysis

This project aims at automation of 2 tasks:
- Collecting user details and tweets of specific hashtags in twitter.
- Collecting user details and tweets of specific @user_mention in twitter.

## Step1
Update the Twitter API credentials in ```twitter_credentials.py```

## Step2
Download the required dependencies
```bash
pip install pandas
pip install tweepy
 ```
 ## Step3
 Run ```user_timeline_tweets.py``` to get user details and tweets of specific @user_mention in twitter. 
 In bash we can run the script using:
 ```bash
 python user_timeline_tweets.py
 ```
 
 Run ```tweepy_streamer.py``` to get user details and tweets of specific hashtags in twitter.
 In bash we can run the script using:
 ```bash
 python tweepy_streamer.py
 ```
