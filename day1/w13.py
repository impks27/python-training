x=[12,45,3,21,78,25]
y=sorted(x)
print(y)

z=sorted(x, key=int, reverse=True)
print(z)

d={'x':1,'z':2,'y':3}
for k in sorted(d):
    print(k, d.get(k))

for k,v in sorted(d.items()):
    print(k,v)


x=[1,2,3,1,3,2,1,2,3,5]
y=set(x)
print(y)
z=list(y)
print(z)


print("SETsssssssssssssssssssssssss")
a=set()
#a=dict()
#a=tuple()
#a=list()
#a=str()
a.add('aaa')
a.add('bbb')
a.add('ccc')
a.add('ddd')
print(a)

a.update(['ppp','qqq','aaa'])

print(a)

if 'aaa' in a:
    print ('found')

print()
print()
print()

a.discard('aaa')

print(a)

b=a.copy()
print(b)
len(a)
max(a)

b={'aaa','qqq'}

#c=a+b // Dict and Sets cannot be added using +

a=[1,2,1,3,4,3,5,1,3,2,1,3,5]
b=[5,6,7,4,5,6,5,4,7,8,9,5]
r=set(a)
s=set(b)
print(r)
print(s)

print(r.union(s))
print(r|s)

print(r.intersection(s))
print(r&s)

print(r.difference(s))
print(r-s)

print(r.symmetric_difference(s))
print(r^s)
