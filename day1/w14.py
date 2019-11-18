#Find occurences
# Approach 1
num=input('Enter the number:')
temp = {i : num.count(i) for i in set(num)} 
print(temp)

# Approach 2
all={}
for i in num:
    if i in all:
        all[i]+=1
    else:
        all[i]=1

print(all)

# Approach 3
n=int(input('Enter the number:'))
k=0
while k<=9:
    s=n
    c=0
    while s!=0:
        r=s%10
        if r==k:
            c+=1
            s=s//10
    if c>0:
        print('%d occurs %d times' % (k,c))
    k+=1
