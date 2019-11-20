#exceptions
import os,sys
os.system ('cls')
try:
    n=int(input('enter a value '))
    print (n)
    try:
        a={'a':1,'b':2}
        b={'a':1,'b':2}
        c=a+b
    except TypeError:
        print ('wrong data type passed to opertaor')
except ValueError:
    print ('wrong input')
except:
    print ('other errors')
    print (sys.exc_info()[0])
    print (sys.exc_info()[1])
else:
    print ('done')
finally:
    k=1
    while k<=3:
        print ('python')
        k+=1
