#find the count of files and sub-dirs
import os
fc=0
dc=0

#picking and storing the directory entries
x=os.listdir('.')

for m in x:
    if os.path.isfile(m):
        fc+=1
    elif os.path.isdir(m):
        dc+=1
print ('%d files and %d dirs' % (fc,dc))
