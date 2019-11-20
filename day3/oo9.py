#mutiple inheritence. 
class A (object):
    def __init__(self):
        self.eno=111
        self.ename='computer'

class B (object):
    def __init__(self):
        self.eno=222
        self.ename='keyboard'

#class C (B,A):
class C (A,B):
    def display(self):
        #A.__init__(self)
        print (self.eno, self.ename)
        
#object creation
x=C()
x.display() # Prints based on the order

#Private functions cannot be inherited
