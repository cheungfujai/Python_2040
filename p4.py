from functools import reduce
def get_average_grades(filename):
	with open(filename, 'r') as file:
		return [reduce(lambda x,y:x+y,list(filter(lambda a:a!=-1,ln)))/len(list(filter(lambda a:a!=-1,ln))) for ln in list(map(list,zip(*[list(map(float,line.split(','))) for line in file])))]
print(get_average_grades('grades.csv'))