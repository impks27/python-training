import os,sys
os.system ('cls')

with open('testfile.txt','r') as fo:
    s=fo.read()
    sys.stdout.write(s)
