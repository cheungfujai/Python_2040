from functools import reduce

def word_count(x, n, str): 
	if (len(x) > n and str in x):
		listtest = (len(x) > n and str in x)
		return listtest

x = ['python is cool','pythom is a large heavy-bodied snake','The python course is worse taking','The python course is worse taking','The python course is worse taking']
print(list(filter(lambda x: word_count(x, 20,'python'), x)))
