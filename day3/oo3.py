#creating an array of objects
import pickle
from wobj import temp
#create an array of three objects
data=[]
k=1
while k<=3:
    data.append(temp())
    k+=1

#accept values
print ('enter values')
k=0
while k<3:
    data[k].accept()
    k+=1

#display values
print ('displaying values')
k=0
while k<3:
    data[k].display()
    k+=1

#write to a file
with open('empdat','wb') as fo:
    pickle.dump(data,fo)

#Read from afile
with open('empdat','rb') as fo:
    data=pickle.load(fo)

k=0
while k<3:
    data[k].display()
    k+=1
