#creating a file from the keyboard. Used ctrl + D after writing to save
import os,sys
os.system ('cls')

#creating a file object
fo=open('testfile.txt','w')


#read the input from keyboard
print('enter text: ')
s=sys.stdin.read()

#write the string into the file
fo.write(s)

#close the file
fo.close()
