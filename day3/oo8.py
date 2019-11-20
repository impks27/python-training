#multilevel inheritence. 
class A (object):
    def __init__(self):
        self.eno=111
        self.ename='computer'

class B (A):
    def accept(self):
        self.ecity='bangalore'
        self.edsgn='manager'

class C (B):
    def display(self):
        print (self.eno, self.ename, self.ecity, self.edsgn)
        
#object creation
x=C()
x.accept()
x.display()

#Private functions cannot be inherited
