import glob
import os
for m in range(1,4):
	for n in range(1,3):
		if m!=n:
			print (m,n)

print()
print()
print()
s=[(m,n) for m in range(1,4) for n in range(1,3) if m!=n]
print (s)

t=[os.path.getsize(m) for m in glob.glob('*.py')]
print(t)

t=sum([os.path.getsize(m) for m in glob.glob('*.py')])
print (t)

q=sum([os.path.isfile(m) for m in os.listdir('.')])
print(q)

print("***********************")

x=[12,34,56,89]
for m in x:
    print (m)

print("For index and value use enumerate")
for i,j in enumerate(x):
    print (i,j)


for i,j in enumerate('computer'):
    print (i,j)

print("Traverse mutiple array")
x=[1,2,3,4]
y=['I','II','III','IV','V']
z=['one','two','three','four']
for p,q,r in zip(x,y,z):
    print (p,q,r)


print("Reverse is slow and the original array is lost")
x=[12,34,5,67]
print(x)
x.reverse()
print(x)
y=reversed(x)
print(y)
print(list(y))


x=os.listdir('.')
print (x)
print (list(reversed(os.listdir('.'))))
 
x=[12,4,3,2,6]
y=sorted(x)
print(y)


x='computer'
y=list(x)
print(y)
z=reversed(y)
print(list(z))

