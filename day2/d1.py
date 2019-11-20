# function

import os
os.system('cls')

# function definition
def f1():
    'my first function'
    k=1
    while k<=5:
        print ('Python')
        k+=1
    return

print ('working with user defined functions')
f1() # function call
print ('done')
print (f1.__doc__)
