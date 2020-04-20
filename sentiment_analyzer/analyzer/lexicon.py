import tweepy
import pandas as pd 
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import csv
from datetime import date

today = date.today()
print(today)

def get_sentiments(search_term):
	consumer_key = 'YOUR_CONSUMER_KEY'
	consumer_secret = 'YOUR_CONSUMER_SECRET_KEY'
	access_token = 'YOUR_ACCESS_TOKEN'
	access_token_secret ='YOUR_ACCESS_TOKEN_SECRET_KEY'

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)
	tweets = api.search(search_term, count=200)
	data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])

	print(tweets[0].created_at)
	sia = SentimentIntensityAnalyzer()
	listy = []

	for index, row in data.iterrows():
		ss = sia.polarity_scores(row["Tweets"])
		listy.append(ss)

	
	se = pd.Series(listy)
	data['polarity'] = se.values 

	list1 = []
	for i in range(0,len(data)):
		list1.append(data['polarity'][i])
	df = pd.DataFrame(list1)
	data['Negative'] = df['neg']
	data['Neutral']   = df['neu']
	data['Positive'] = df['pos']
	data['Compound'] = df['compound']


	data.to_csv(f'{today}_data.csv')
	total_neg = 0
	total_neu = 0
	total_pos = 0
	total_com = 0


	labels = ['Negative','Neutral','Positive','Compound']
	for i in range(0,len(data['polarity'])):
		total_neg += data['Negative'][i]
		total_neu += data['Neutral'][i] 
		total_pos += data['Positive'][i]
		total_com += data['Compound'][i]

	total_neg = format(total_neg,'.2f')
	total_pos = format(total_pos,'.2f')
	total_neu = format(total_neu,'.2f')
	total_com = format(total_com,'.2f')		

	return total_neg,total_neu,total_pos,total_com	



