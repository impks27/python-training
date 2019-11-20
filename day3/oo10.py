#hierarchical inheritence. 
class A (object):
    def __init__(self):
        self.eno=111
        self.ename='computer'

class B (A):
    def output(self):
        print (self.eno, self.ename)

class C (A):
    def display(self):
        print (self.eno, self.ename)
        
#object creation
x=B()
x.output() 

y=C()
y.display() 
