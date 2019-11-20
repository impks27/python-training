#class level attributes
class temp (object):
    'this is my first class creation'
    def accept(self):
        self.eno=111
        self.ename='computer'
    def display(self):
        print (self.eno, self.ename)

x=temp()

x.accept()
    
#class level
print ('Name of the class is:', temp.__name__)
print ('Base of class is:', temp.__bases__)
print ('the module in which the class is:', temp.__module__)
print ('the doc string of the class is:', temp.__doc__)
print ('info about the class is:', temp.__dict__)


#object level
print (hasattr(x,'eno')) #Will be False if accept() is not called
setattr(x,'ecity','bnglr')
print (x.ecity)
delattr(x,'ecity')
