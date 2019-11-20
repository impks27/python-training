# passing args to a function
def f1(x):
    for k,v in sorted(x.items()):
        print (k,v)
    return

import os
os.system ('cls')
d={'x':1,'z':2,'y':3}
f1(d)
print('done')
        
