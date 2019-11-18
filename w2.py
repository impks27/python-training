#file or directory
import os
n=input('name')
if os.path.isfile(n):
    print('%s is a file' % n)
elif os.path.isdir(n):
    print('%s is a directory' % n)
else:
    print('some other entry')
