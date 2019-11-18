#find the sum of sizes of python files
#find the count of files and sub-dirs
import os
s=0

#picking and storing the directory entries
x=os.listdir('.')

for m in x:
    if os.path.isfile(m) and m[-3:]=='.py':
        t=os.path.getsize(m)
        s+=t
print (s)
