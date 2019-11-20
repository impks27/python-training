#reading from a file
import os,sys
os.system ('cls')

#create file object
fo=open('testfile.txt','r')

#read from file into a string
s=fo.read()

#display the content
sys.stdout.write(s)

#close the file object
fo.close()
