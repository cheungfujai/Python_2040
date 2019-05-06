
tcredit=0
totalgpa=0

instr=""
try:
	instr= raw_input()
	gpa,credit=map(float,instr.split())
except ValueError:
	gpa=float(instr)

if gpa != -1:
	while (gpa<0 or credit<0) and gpa!=-1:
		print("Wrong input!")
		try:
			instr= raw_input()
			gpa,credit=map(float,instr.split())
		except ValueError:
			gpa=float(instr)
	if gpa != -1:
		totalgpa+=gpa*credit
		tcredit+=credit
		ngpa=totalgpa/tcredit
		print("Current GPA: {0:.2f}".format(ngpa))
while gpa !=-1:
	try:
		instr= raw_input()
		gpa,credit=map(float,instr.split())
	except ValueError:
		gpa=float(instr)
	if gpa != -1:
		while (gpa<0 or credit<0) and gpa!=-1:
			print("Wrong input!")
			try:
				instr= raw_input()
				gpa,credit=map(float,instr.split())
			except ValueError:
				gpa=float(instr)
		if gpa != -1:	
			totalgpa+=gpa*credit
			tcredit+=credit
			ngpa=totalgpa/tcredit
			print("Current GPA: {0:.2f}".format(ngpa))
print("Program ends.")