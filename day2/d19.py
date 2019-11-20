#processing a file
import os,sys,time
os.system ('cls')

with open('testfile.txt','r') as fo:
    for m in fo:
        print(m.upper(),end="") #don't end wih newline
        time.sleep(2)
