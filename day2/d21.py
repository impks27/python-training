#reading into a list
import os,sys
os.system ('cls')

with open('testfile.txt','r') as fo, open('xyzfile.txt','w') as fo1:
    a=fo.readlines()
    print (a)
    fo1.writelines(a)
