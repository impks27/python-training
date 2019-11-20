#filter.
def f1(x):
    return x%2!=0

print (list(filter(f1,range(111,120))))

def prime(n):
    import math
    k=2
    s=1
    while k<=math.sqrt(n) and s==1:
        r=n%k
        if r==0:
            s=0
        k+=1
    if s==1:
        return n

r=prime(11)
print (r)
r=prime(12)
print (r)

print(list(filter(prime,range(11,20))))
