#Passing function as argument
def f1(p,q):
    return (p+q)

def f2(s,t):
    return (s-t)

def f3(x,y):
    m=10
    n=12
    r1=x(m,n)
    r2=y(m,n)
    return (r1+r2)

r=f3(f1,f2)
print (r)
