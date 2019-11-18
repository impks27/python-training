#Reading env 
import os
x=os.environ
for m in x:
    print ('%-30s   %-40s' % (m,x.get(m)))
    
