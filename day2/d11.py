#Map
def f1(x):
    return (x**2)
print (list(map(f1,[1,2,3,4,5])))

def f2(x,y):
    return (x*y)
print (list(map(f2,range(1,10),range(11,20))))
