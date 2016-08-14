#ex5_5.py
def divide(num):
	cent=[0,0,0,0]
	level=[25,10,5,1]
	for i in range(len(cent)-1):
		cent[i]=num/level[i]
		num=num-cent[i]*level[i]
	cent[len(cent)-1]=num
	return cent
