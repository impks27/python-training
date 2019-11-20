#Alternate lines in uppercase
import os,sys,time
os.system ('cls')

with open('testfile.txt') as fo: #no mode mentioned means r by default
    k=0
    for m in fo:
        if k%2==0:
            m=m.upper()
        print(m,end="")
        k=k+1

