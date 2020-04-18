from django.shortcuts import render
from django.http import JsonResponse
from .lexicon import get_sentiments

def home(request):
	return render(request,'home.html')


def getchart(request):
	term = request.GET['term']
	neg,neu,pos,com = get_sentiments(term)
	print(neg)
	print(neu)
	print(pos)
	print(com)
	data = {
		'neg':neg,
		'neu':neu,
		'pos':pos,
		'com':com,
	}
	return render(request,'chart.html',{'neg':neg,'neu':neu,'pos':pos,'com':com})


