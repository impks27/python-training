k=1
n=5
while k<=12:
    print ('%d * %d = %d' % (n,k,k*n))
    k+=1

print()
print()

k=1
n=5
while True:
    print ('%d * %d = %d' % (n,k,k*n))
    k+=1
    if k>12:
        break
