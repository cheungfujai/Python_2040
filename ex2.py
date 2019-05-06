import sys


a=int(raw_input("Enter an integer: "))
if a != -1:
	str=raw_input("Enter a string:")
	for i in range(1,a+1):
		for j in range(0,i):
			sys.stdout.write(str)
		sys.stdout.write("\n")
	sys.stdout.write("\n")

while a!=-1:
	a=int(raw_input("Enter an integer: "))
	if a != -1:
		str=raw_input("Enter a string:")
		for i in range(1,a+1):
			for j in range(0,i):
				sys.stdout.write(str)
			sys.stdout.write("\n")
		sys.stdout.write("\n")
print("Program ends.")