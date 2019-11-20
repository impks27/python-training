# Using modules
from wmod import f1 as ab,x
# Using from helps in loading particular defns helping in less memory load
from wmod2 import f1 as ac
print ('calling functions')
#f1() To avoid the error for this we alias
ab()
ac()
print (x)
