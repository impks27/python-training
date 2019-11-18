#disply the size of python file
import os
n=input('name')
if os.path.isfile(n) and n[-3:]=='.py':
    print ('%s is a python file' % n)
    s=os.path.getsize(n)
    print('%s has %d bytes' % (n,s))
else:
    print ('not a python file')
