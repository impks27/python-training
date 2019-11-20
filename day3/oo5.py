#Varibale which starts with __ is private
class temp (object):
    'this is my first class creation'
    def accept(self):
        self.__eno=111
        self.__ename='computer'
        self.__display()
    def __display(self): #private method
        print (self.__eno, self.__ename)

x=temp()
x.accept()
#print (x.eno, x.ename) # Gives error as the vars are private
#x.display() # Error

