import tweepy
import pandas as pd 
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import csv
from datetime import date

today = date.today()
print(today)

def get_sentiments(search_term):
	consumer_key = '1o3lLkjCh4Agn0CYXEIksEzbd'
	consumer_secret = '3qSeXizsz2LkR9ZUOdgHcjzpkTpz7zbnELoXI8G92R4Jm3E9y4'
	access_token = '3289885325-gFG44n98E8JW12vIkq177hIrG7KvacIvwiIjPcX'
	access_token_secret = 'WyJ96v1tjFJrQqkx6ItKDd3gO4XD2lsoPrhj4ouJvbkT5'

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


	data.to_csv(f'C:\\Users\\Asus\\Desktop\\sentiment_analyzer\\Data\\{today}_data.csv')
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



