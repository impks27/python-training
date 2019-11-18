#Check Armstrong number
n=int(input('enter number'))
s=0
temp=n
while temp>0:
    rem=temp%10
    s+=rem**3
    temp//=10
if s==n:
    print("This is Armstrong number")
else:
    print("This is not Armstrong number")
