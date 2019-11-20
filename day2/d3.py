#call by value and call by reference

#If we pass immutable objects, it is call by valye.
def f1(x,y):
    temp=x
    x=y
    y=temp
    print (x,y)
    return

m=10
n=12
print (m,n)
f1(m,n)
print (m,n)

#If we pass mutable objects, it is call by ref.
def f2(a):
    a.append(100)
    print (a)
    return

p=[1,2,3,4]
print (p)
f2(p)
print (p)
