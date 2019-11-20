"# python-training" 
Day-1
=========
Freatures:
1.built on C api
2.compiled interpreted language(line by line compilation)
3.Portable
4.object oriented(classes and object).
5.interfacing with other languages/tools.
6.extensible
7.dynamic programming(running laungage..during excution only creates req things)
8.easy to use and debug.

1.)PY FUNDAMENTALS:(2.7, 3.7)-here working with 

datatypes:
a)number: any integer/float(+ve/-ve), complex value.
Ex:x=123, y=12.345, x-3-4j
b)string: anything enclosed in single or double wuotes,multiline strings allowed. string cannot be changed once created, immutable and unlimited.
mutline string: start and end with(''' and """)
Ex:x='hp', y="complex"
x='''this is my
multiline
string'''
c)list:dynamic array. created with [], elements can be any type, and are separated by comma. unlimited and mutable(can change).
Ex:
x=[1,2.3,'abc','abc',[1,2,3]]
d)tuple: static array, created with (), elements can be any type, and are separated by comma. unlimited but immutable(cannot change).
Ex:{1,'abc',[1,2,3], (7,8,9))
e)dictionary: key value pairs . created with {}, keys are unique and quoted, unlimited and mutable(can be changed)
Ex:
x={'a':1,'b':'abc','c':[1,2,3],'d':(4,5,6),'e':{'m':1,'n':2}}
note: dcitionary is unorderd data

Variables: these are known as references
Rules:
1.no declaration
2.case sensitive
3.globle by default
creating varibles:
 variable=value
x=123
x='abd'
x=[1,2,3]
x=(2,3,4)
x={'a':1, 'b':'abc'}
To remove variable
del(x)

string reverse: x[::-1]
toget second char of string in reverse order: x[::-2]
toget last 3 char: x[-3:]

number floating values:
x=12.345
y=float(x)
y=int(x)

a=3-4j (complex class)
a=complex(-2,3)
print(a)
(-2+3j)

multiline stiring:
z='''this is 
my first py 
program'''

Lists:
x=[1,'abc',[3,4,5]]
x[2][1]
print x
4

Tuple:
x=(1, 'abc',[3,4,5],(7,8,9))

list, Dict--mutable
str, tuple, number---immutable

datatype:
Sequences: str, tuple, number
collections: list, dict

dictionary:
x={'a':1, 'b':'abc','c':[1,2,3],'d':(6,7,8), 'e':{'m':1, 'n':2}}
del x['e']


2.)OPERATORS and CONTROL FLOW
a)arthematics  +,-,*,/,%, **
b)relational  >,>=,<,<=,++, !=<>
c)logical  and, or, not
d)assignment  k=10, k+=20
              +=,-=,*=,/=,%=,**=
e)identity   is, is not(ids are same)
             x is y (id(x is id(y)     True / false
             x is not y (id(x) is not id(y))
f)membership  in, not in
              x='computer'
              'm' in x
              
              a=34
              b=[12,34,56,]
              a in b
g)boolean   Treu/False

h)contrtol flow operators:
  if , for, while
-->if 
  if condition:
     stmt
  
  if condition:
     stmt
  else:
     stmt

  if condition:
     stmt
  elseif condition:
    stmt
  elseif conditon:
    stmt:
  else:
    stmt:
-->For
x=[1,2,3,4]
for m in x:
  print(m)

-->While

3)DATA OBJECT BASED FUNCTIONS

a)Dictionary functions:
d={'a':1,'b':2,'c':3}
d.keys()-->keys a,b,c
d.values()--> values 1,2,3
d.items()-->each pair

e=d.copy() ---> to copy dictionary
e.clear()---> to clear diciotnary
d.pop('b')---> to remove key 'b'(values also be cleared along with key)
d.get('a')--> to get value associated with 'a'

d.update(e)---> updating d dictionay with e dictionary
b)List functions
x=[23,5,67,89]
max(x)
min(x)
len(x)
y=[1,2,3]
z=x+y

a='computer'
b=list(a)
print b
['c','o'......]

x.append(120)---> to append value at end of list
x.insert(0,111)---> to insert 111 at index 0 place
x.pop(2) ---> to clear index values of 2
x.pop()---> clear end index value
x.extend(y)----> adding y list to x list
y=x.copy()--> to copy x list to y (it will create new one with diff address)
x.reverse()--> the list will be reversed
x.index(67)--> to know index of 67
x.count(67)--> to count the 67 number in x list
x.sort()--> asending order by default
x.sort(key=str,reverse=True)---> desending order sorting

c)Tuple

x=(1,2,2,3,2,1,1)
x.count()
x.index(3)

d)strings
x='computer'
x.upper()---> address will not be changed as it is only displying
y=x.upper()--> address will be changing here
x.title()--> first char of each word is capital
x.capitalize--> first char of line is capital
x='HP Computer'
x.swapcase()--- o/p hp cOMPUTER
x='information'
x.find('i')-- o/p 0
x.count('i')
x.rfind('i')---> tofind i in reverse order
x.replace('for','FOR')-- o/p inFORmation
x.center()

x='computer'
x.startswith('com')--> op true
x.lstrip()
x.rstrip()
x.strip()
x.endswith()
y=x.split()
'-'.join(y)----> joining of word of y string with - (hyphen)
x.islower()
x.isupper()
x.isdigit()
x.isalnum()
x.isalpha()
x.isspace()
encode()
decode()

d)Integer:
import math
math.sqrt(144)
math.factorial(4)
math.floor()
math.ceil()
math.log()

dir(math)--> to check fuctions available in math module

4)SETS, LOOPING TECHNIQUES, LIST COMPREHENSIONS(very useful and popular)

range(5)
range(0,4)
s=[(m,n) for m in range(1,4) for n in range(1,3) if m!=n]
op: [(1,2),(2,1),(3,1), (3,2)]

import glob
t=[os.path.getsize(m) for m in glob.glob('*.py')]

s=sum([os.path.getcount(m) for m in os.listdir('.')])

enumerate:
---------------------------
x=[12.24.36.48]
for i,j in enumerate(x):
    print(i,j)
Note: enumerate gives both index and value for integers/string
----------------------------

zip:

x=[1,2,3,4]
y=['I','II','III','IV']
z=['one','two','three','four']

for p,q,r in zip(x,y,z)
    print (p,q,r)

o/p:
1 I one
2 II two
3 III three
4 IV four
-------------------------

x=[12,24,36,48]
x.reverse()

reversed:
x='computer'
y=reversed(x)
print(y)
z=str(y)
print(z)
it will reverse at the same address

for list of huge
list(reversed(os.lisrdir('.')))

sorted:
x=[12,45,3,21]
y=sorted(x)--> asending order sorting-original array will not be changed or disturbed
z=sorted(x, key=int, reverse=true)---> to sort in desending order

dictionary sorted:

d={'x'=1,'y'=2,'z'=3}
  for k in sorted(d):
      print(k,d.get(key))

x=[1,2,3,1,3,2,1,2,1,3,5]
y=set(x)--> unique elements will be displyed
op: {1,2,3,5}

set is un orderd collection of elements

a=set()--> create empty list
a=str()
a=list()
a=tuple()
a=dict()
a=set()
a.add('aaa')--> to add single element
a.add('bbb')
print(a)
op: {'aaa', 'bbb'}
a.update(['ppp','ddd'])---> to add mutilple elements
a.discard('ccc')---> to remove element
len(a)
max(a)
min(a)

where do we sets: to eleminate duplicate

a=[1,2,3,4,5.3]
b=[9,8,7,3]
r=set(a)--to remove duplicates in list a
s=set(b)--to remove duplicates in list b
r.union(s)---> to give union

r.intesection(s)--> to give common elemts of s and r lists
r.difference(s)--> to give diff elements of s and r list
r^s gives same result of r.difference(s)
program:

cricket={'p,'r','ramesh','ranga'}

DAY-2
==========================
5) USER DEFINED FUNCTIONS
a)built in
b)additional
c)user defined

Function has 3 parts
1.declaration or prototype
2.defination or function body
3.execution or function call
A. function is a sub programm that can be called repetitively

How to define a function

def funname():
    stmt
    return

how to call the function?
r=funname(args)
funname(args)
