# global and local variable in function
k=111
print (k)

def f1():
    k=222
    print (k)
    global m
    m=k+globals()['k']
    print (m)
    print (locals())
    return

f1()
print (k)
print (globals())
print (m)
