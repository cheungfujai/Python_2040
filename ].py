from functools import reduce

def test(x, n, str):
	if (len(x) > n and str in x):
		listtest = (len(x) > n and str in x)
		return listtest

def word_count(x, n, str): 
	return (reduce(lambda a,b:a+","+b, (list(filter(lambda x: test(x, n, str), x)))).count(str))
