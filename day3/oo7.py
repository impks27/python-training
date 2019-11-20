#Single inheritence
class A (object):
    def __init__(self):
        self.eno=111
        self.ename='computer'

class B (A):
    def display(self):
        print (self.eno, self.ename)

#object creation
x=B()
x.display()
