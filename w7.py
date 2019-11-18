import os,glob
x=glob.glob('*.py')
s=0

for m in x:
    t=os.path.getsize(m)
    s+=t    
print (s)
