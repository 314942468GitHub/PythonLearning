#use to test ex5_6
from ex5_6 import *
oper = ["+","-","*","/","%","**"]
for i in range(len(oper)):
	for j in range(1,10):
		for k in range(1,10):
			string=str(j)+" "+ oper[i]+" "+str(k)
			print str(j),oper[i],str(k),"=",algorism(string)
