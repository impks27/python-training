import os,sys,shutil,datetime
for root, dirs, files in os.walk('.\p1'):
    print (root)
    for m in files:
        m=root+'\\'+m
        print (m)
    print()


print(sys.platform)
print(sys.version)

#shutil.copytree('p1','q1')
#os.listdir('q1')

x=datetime.datetime.now()
print(x.strftime('%d-%m-%Y'))
print(x.strftime('%H:%M:%S'))

#Add 100 days to current date

x=datetime.date.today()
print(x)
p=datetime.timedelta(days=100)
z=x+p
print(z)

#Any date
y=datetime.date(2019,11,20)
p=datetime.timedelta(days=365)
z=x+p
print(z.strftime('%d-%m-%Y'))

#Diff between dates:
from dateutils import relativedelta as rd
x=datetime.date(2000,1,31)
y=datetime.date.today()
z=rd(y,x)
print('%d years %d months %d days ' % (z.years,z.months,z.days))

#Add five months to date
s=rd(months=5)
z=y+s
print(z)

