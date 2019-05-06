number = [0] * 4
namelist = ['first', 'second', 'third', 'fourth']

for i in range(len(number)):
	number[i] = raw_input('Please input the '+str(namelist[i])+' number: ')
	while number[i].isdigit() == False:
		print("Your input is not a number!")
		number[i] = raw_input('Please input the '+str(namelist[i])+' number: ')
	
number.sort()
print('The second smallest value is ', sorted(number)[1])
print('Program ends.')