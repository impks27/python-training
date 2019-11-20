#Predefined class 'object' in python. Every class we create inherits object
#class definition
class temp(object):
    def accept(self): #self is object ref. 
        self.eno=int(input('enter eno:'))
        self.ename=input('enter ename:')

    def display(self):
        print (self.eno, self.ename)

#object creation
x=temp()

#calling methods
x.accept()
x.display()
