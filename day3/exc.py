#exceptions
import os,sys
os.system ('cls')
try:
    n=int(input('enter a value '))
    print (n)
except:
    print ('wrong input')
    print (sys.exc_info()[0])
    print (sys.exc_info()[1])
k=1
while k<=3:
    print ('python')
    k+=1
'''
>>> print(n)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(n)
NameError: name 'n' is not defined
>>> print('fjbef)
      
SyntaxError: EOL while scanning string literal
>>> x=[1,2,3]
>>> x[6]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    x[6]
IndexError: list index out of range
>>> fo=open("wewfewf")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    fo=open("wewfewf")
FileNotFoundError: [Errno 2] No such file or directory: 'wewfewf'
>>> x={'a':1,'b':2}
>>> x['d']
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    x['d']
KeyError: 'd'
>>> x=1/0
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    x=1/0
ZeroDivisionError: division by zero
'''
