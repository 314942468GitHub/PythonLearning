from ctypes import *
import os 

cal = cdll.LoadLibrary(os.getcwd() + '/build/lib.macosx-10.12-intel-2.7' +'/cal.so') 

for i in range(10):
    for j in range(10):
        print "%d + %d = %d" %(i,j,cal.add(i,j)) + ';'\
        "%d - %d = %d" %(i,j,cal.minus(i,j)) + ';'\
        "%d * %d = %d" %(i,j,cal.multiply(i,j)) + ';'\
        "%d / %d = %d" %(i,j,cal.divid(i,j))

