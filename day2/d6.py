# Function call with specofic values
import os
def f1(x,y,z):
    return sum([x,y,z])

r=f1(z=10,x=12,y=14)
print (r)

def xyz(fname,fext):
    r=fname+'.'+fext
    s=os.path.getsize(r)
    print (s)
    return

xyz(fname='d6',fext='py')

def f1(y,z,x=121): #default value assignment should be from right
    return sum([x,y,z])

r=f1(z=10,y=14)
print (r)
