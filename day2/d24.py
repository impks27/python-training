#Delete odd lines from a file
import os,sys,time,shutil
os.system ('cls')

with open('testfile.txt','r') as fo1, open('updatedfile.txt','w') as fo2: #no mode mentioned means r by default
    k=0
    for m in fo1:
        if k%2!=0:
            fo2.write(m)
        k=k+1
shutil.copy('updatedfile.txt','testfile.txt')
