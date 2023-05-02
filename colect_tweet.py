# imports
import tweepy
import pandas as pd
import numpy as np
import time
import re
from litwallet import app,mysql
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer    
from cleantext import clean
import demoji


analyzer = SentimentIntensityAnalyzer()
consumer_key = 'Xyxa9A8lYPlQehlMHH83vPHCX'
consumer_secret = 'y1Mo08l4rVbTGxaOJI2NjJjkboHDRoc6aYWIzrDAqbfAgWhJAn'
access_token = '1493532560642781189-3BOlNc99QivZ9Ae9gAP4zM8UFxsEoW'
access_token_secret = 'gni9a1kP7cZH1GxMjNs5FA6CiD15de6oNhEudIq3Ttc3R'
KEY = "7JWIUY69T87W83GH"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

def initialize():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser = tweepy.parsers.JSONParser())
    return api
# api = initialize()

def sercher(times, id):
  print("Tweet aquisation in progress please wait............. ")
  comp_searches = ("@FXstreetNews", "@ForexLive", "@ForexFactory", "@FOREXcom", "@BTCTN", "@Bitcoin", "@ethereum",)
  sentiments = []# Iterate through all the comp_searches
  for search in comp_searches:
        
      # Bring out the 100 tweets
      if id == 0:
        comp_tweets = api.user_timeline(screen_name=search, count=times)
      else:
        comp_tweets = api.user_timeline(screen_name=search, count=times, max_id=id)
      
      # Loop through the 100 tweets
      for tweet in comp_tweets:
          text = tweet["text"]
          
      # Add each value to the appropriate array
          sentiments.append({"User": search,
                            "text":text,
                        "Date": tweet["created_at"],
                        "id": tweet["id"]
                          })
  return sentiments

def remove_pattern(input_txt, pattern):
    r = re.findall(pattern, input_txt)
    for i in r:
        input_txt = re.sub(i, '', input_txt)        
    return input_txt

def clean_tweets(tweets):
    print("##################: Cleaning in progress please wait............. :############################")
    #remove twitter Return handles (RT @xxx:)
    tweets = np.vectorize(remove_pattern)(tweets, "RT @[\w]*:") 
    
    #remove twitter handles (@xxx)
    tweets = np.vectorize(remove_pattern)(tweets, "@[\w]*")
    
    #remove URL links (httpxxx)
    tweets = np.vectorize(remove_pattern)(tweets, "https?://[A-Za-z0-9./]*")
    
    #remove special characters, numbers, punctuations (except for #)
    tweets = np.core.defchararray.replace(tweets, "[^a-zA-Z]", " ")
    
    return tweets

def create_new_columns(current_df, column):
  print("##################: Column Creation in progress please wait............. :############################")
  new_df = []
  count = int(current_df.size/4)
  try:
    for i in range(count):
      text = current_df['text'][i]
      vs = analyzer.polarity_scores(text)
      new_df.append(vs[column])
  except ValueError as e:
    pass
  except KeyError as e:
    pass
  return new_df

def my_main(x):
  print("##################: Main Execution in progress please wait............. :############################")
  y = x*2-1
  cols = ["pos","neg","neu","compound"]
  for i in range(10):
    if i > 1:
      frames = [df1,df2]
      df1 = pd.concat(frames)
      df2 = pd.DataFrame.from_dict(sercher(x, df1["id"].iloc[-1]))
      for j in cols:
        new_df = create_new_columns(df2,j)
        df2[j] = new_df
    elif i == 1:
      df2 = pd.DataFrame.from_dict(sercher(x, df1["id"].iloc[-1]))
      for j in cols:
        new_df = create_new_columns(df2,j)
        df2[j] = new_df
    else:
      df1 = pd.DataFrame.from_dict(sercher(x, 0))
      for j in cols:
        new_df = create_new_columns(df1,j)
        df1[j] = new_df
  return pd.concat([df1,df2])


def inserter():
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
    tf1 = pd.read_csv("/content/drive/MyDrive/Envs/Flaskt/flaskt/x4.csv")
    print(len(tf1))
    with app.app_context():
                    cursor = mysql.connection.cursor()
                    with  cursor as f:
                        for i in range(1,len(tf1)-1):
                            tid = tf1['id'][i]
                            user = tf1['User'][i]
                            # tweet = demoji.replace(tf1['text'][i])
                            tweet =  re.sub('[^A-Za-z0-9]+', ' ', tf1['text'][i])
                            time = tf1['Date'][i]
                            sentiment = tf1['compound'][i]
                            smt = f"INSERT INTO tweets(time, user, tweet, sentiment) VALUES('{time}', '{user}', '{tweet}', {sentiment});"
                            print(smt)
                            f.execute(smt) 
                    mysql.connection.commit()
                    cursor.close()

inserter()
