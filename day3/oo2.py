#Predefined class 'object' in python. Every class we create inherits object
#class definition
class temp(object):
    def accept(self,a,b): #self is object ref. 
        self.eno=a
        self.ename=b

    def display(self):
        print (self.eno, self.ename)

#object creation
x=temp()

#calling methods
x.accept("100","Computer")
x.display()
