#ex5_3.py
def scoreLevel(score):
	if score > 100 or score < 0:
		print "Socre Error!"
		return -1
	elif score >= 90:
		return "A"
	elif score >= 80:
		return "B"
	elif score >= 70:
		return "C"
	elif score >= 60:
		return "D"
	else:
		return "F"
