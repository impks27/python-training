#method overriding
class A (object):
    def __init__(self):
        self.eno=111
        self.ename='computer'
    def display(self):
        print ('displaying from class A')
        print (self.eno, self.ename)

class B (A):
    def display(self):
        print ('displaying from class B')
        print (self.eno, self.ename)

        

x=B()
x.display() 

