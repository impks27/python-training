import os,re
os.system ('cls')

with open('regex.txt','r') as fo:
    for x in fo:
        m=re.search('python',x)
        if not m:
            print (x,end="")

print ("********************")

with open('regex.txt','r') as fo:
    for x in fo:
        m=re.search('python',x)
        if m:
            print (x,end="")

print ("********************")

with open('regex.txt','r') as fo:
    for x in fo:
        m=re.search('^python',x)
        #if not m:
        if m:
            print (x,end="")
            
print ("********************")

with open('regex.txt','r') as fo:
    for x in fo:
        m=re.search('(a|i)s$',x)
        #if not m:
        if m:
            print (x,end="")
            
print ("********************")

x='python has wxpython pythontk as the powerful gui tools'
m=re.findall('python',x)
print (m)

print ("********************")

x='python has wxpython pythontk as the powerful gui tools'
m=re.findall('[a-z]*python[a-z]*',x)
print (m)

print ("********************")

with open('regex.txt','r') as fo:
    for x in fo:
        m=re.findall('python',x)
        if len(m)>=2:
            print (x,end="")

print ("********************")

x='AAA 080-123456 bnglr'
m=re.search('([A-Z]+) ([0-9]+)-([0-9]+) ([a-z]+)',x)
print (m)
print (m.group(1))
print (m.group(2))
print (m.group(3))
print (m.group(4))
print (m.group(1,4))

print ("********************")

with open('regexdata.txt','r') as fo:
    for x in fo:
        m=re.search('([A-Z]+) ([0-9]+)-([0-9]+) ([a-z]+)',x)
        if m:
            print (m.group(1,4))

print ("********************")
print ("Best way when regex is big. So we separate and compile")
s='([A-Z]+) ([0-9]+)-([0-9]+) ([a-z]+)'
t=re.compile(s)
with open('regexdata.txt','r') as fo:
    for x in fo:
        m=re.search(t,x)
        if m:
            print (m.group(1,4))
    re.purge() #Clears the regular exp buffer

print ("********************")

x='python and Python are same'
print(m)
m=re.sub('python','PYTHON',x)
print(m)
m=re.sub('python','PYTHON',x,re.I) # Not working so check description
print(m)
help(re.sub)
m=re.sub('python','perl',x,2,re.I)
print(m)
print ("********************")


