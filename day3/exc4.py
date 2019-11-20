#User defined exceptions
import os,time
from werr import MyError, ValueSmall, ValueLarge

while True:
    os.system ('cls')
    try:
        n=int(input('enter a value'))
        if n<12:
            raise ValueSmall
        elif n>12:
            raise ValueLarge
        else:
            print ('You gave corect value')
            time.sleep(2)
            break
    except ValueSmall:
        print ('less than 12 entered')
    except ValueLarge:
        print ('more than 12 entered')
    except:
        print ('unknown error')
    time.sleep(3)
