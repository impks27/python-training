# function overloading
# here * is used for tuple which is infinite and read only
def f1(*p):
    return sum(p)

r1=f1()
print (r1)

r2=f1(1,2,3)
print (r2)

r3=f1(1,2,3,4,5,6,7,8,9)
print (r3)
