#ex5_4
def isLeapYear(year):
	if year % 400 == 0:
		return True
	elif (year % 4 == 0) and (year % 100 != 0):
		return True
	else:
		return	False
