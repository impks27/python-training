#display message based on system time
import datetime
x=datetime.datetime.now()
z=x.hour
if z<12:
    print ('Good Morning')
elif z<17:
    print ('Good Afternoon')
elif z<21:
    print ('Good Afternoon')
else:
    print ('Good Night')
