#ex5_6.py
def algorism(inStr):
	string = inStr.split(" ")
	num1 = float(string[0])
	num2 = float(string[2])
	oper = string[1]
	if(cmp(oper,"+")==0):
		return num1 + num2
	elif(cmp(oper,"-")==0):
		return num1 - num2
	elif(cmp(oper,"*")==0):
		return num1 * num2
	elif(cmp(oper,"/")==0):
		return num1 / num2
	elif(cmp(oper,"%")==0):
		return num1 % num2
	elif(cmp(oper,"**")==0):
		return num1 ** num2
	else:
		print "Operation is not correct!"
		return -1
