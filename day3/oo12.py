#operator overloading
class vector (object):
    def __init__(self,a):
        self.first=a
        
    def __add__(self,other):
        self.first.update(other.first)
        return self.first
        

m={'a':1,'b':2,'c':3}
n={'x':4,'y':5,'z':6}

p=vector(m)
q=vector(n)

r=p+q
print (r)
