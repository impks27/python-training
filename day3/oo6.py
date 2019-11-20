#constructors and destuctors"
class temp (object):
    def __init__(self): #constructor
        self.eno=111
        self.ename='computer'
    def display(self):
        print (self.eno, self.ename)
    def __del__(self): #called aut when run from prompt
        print ('object destroyed')

x=temp()
x.display()
del (x)
