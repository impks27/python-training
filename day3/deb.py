#python debugging
# Use n,s,c,q,l,w,p,b,q,enable,!,disable,clear https://docs.python.org/3/library/pdb.html
import os, pdb;
pdb.set_trace()
a=1
b=2
c=3
d=(a+b+c)
print(d)
def abc():
    k=1
    l=2
    if (k==l):
        print ('equal')
    else:
        print ('not equal')

print ('Call Fucntion')
abc()
