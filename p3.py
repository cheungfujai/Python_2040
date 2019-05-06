import os
from os import listdir
import sys
import re
filelist = [file for file in listdir(os.getcwd())]
char=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
inputfile=sys.argv[1]
outputfile=sys.argv[2]

o = open(outputfile, "w")
#preprocess inputfile string
inputfiles=""
hasregex=0
for i,x in enumerate(inputfile):
	if(x=="*"):
		inputfiles=inputfiles+"."
		hasregex=1
	elif x=="?":
		inputfiles=inputfiles+"."
		hasregex=1
	inputfiles=inputfiles+x
inputregex=re.compile(inputfiles+"$")
has=0
count=0
# for i,x in enumerate(filelist):
# 	if(re.match(inputregex,x)!=None):
# 		count=count+1
filelist.sort()
for i,x in enumerate(filelist):
	if(re.match(inputregex,x)!=None):
		has=1
		fileobject=open(x,"r")
		data=[]
		data=fileobject.readlines()
		charactern=0
		wordn=-1
		linen=len(data)
		for i2,y in enumerate(data):
			for z in y:
				if(z in char):
					charactern=charactern+1
			wordn=wordn+len(y.split(" "))
		if(hasregex==1):
			o.write("Name of file: "+x+".\n")
		o.write("Number of characters: "+str(charactern)+".\n")
		o.write("Number of words: "+str(wordn)+".\n")
		o.write("Number of lines: "+str(linen)+".\n")
		fileobject.close()
if(hasregex==0 and has==0):
	print("Opening file "+inputfiles+" failed!")
	exit(0)
elif(has==0):
	print("No matching!")

o.close()