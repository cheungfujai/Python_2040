from functools import reduce
def get_average_grades(filename):
	with open(filename, 'r') as file:
		# x=[[list(filter(lambda a:a!=-1 , ln))] for ln in [list(map(list,zip(*[list(map(int,line.split(','))) for line in file])))]]
		#x=list(map(list,zip(*[list(map(int,line.split(','))) for line in file])))
		#x = [list(map(int,line.split(','))) for line in file]
		#for line in file:
			#print(list(map(int,line.split(','))))
		#print(x)
		#x=[list(map(lambda a:0 if a==-1 else a,ln)) for ln in list(map(list,zip(*[list(map(int,line.split(','))) for line in file])))]
		# x=[reduce(lambda x,y:x+y,list(map(lambda a:0 if a==-1 else a,ln)))/len(ln) for ln in list(map(list,zip(*[list(map(int,line.split(','))) for line in file])))]
		return [reduce(lambda x,y:x+y,list(map(lambda a:0 if a==-1 else a,ln)))/len(ln) for ln in list(map(list,zip(*[list(map(int,line.split(','))) for line in file])))]
get_average_grades('test.csv')