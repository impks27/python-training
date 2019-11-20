#copying of the file
import os,sys
os.system ('cls')

with open('testfile.txt','r') as fo1, open('newfile.txt','w') as fo2:
    s=fo1.read()
    fo2.write(s)
    
