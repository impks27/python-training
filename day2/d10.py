#Function can be assigned, created and removed
def f1():
    print ('you are in f1')

f1()
x=f1
del (f1)
x() #closures in python
#f1()

p=[1,'abc',x]
print (p)

#map, filter, lambda
