#lambda. For small functions instead of going to the function and executing
# and coming back, it is better to copy the code at the pace of the call.
# This is inline function in C++ or lamnda in python
s=lambda x:x**2
print (s(10))

r=s(10)
print (r)

x=[('a',3),('c',2),('b',1)]
y=sorted(x)

print (y)


z=sorted(x,key=lambda x:x[1])
print (z)
