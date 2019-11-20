#function inside function
def f1():
    print ('you are outside function')
    def f2():
        print ('you are in inner function')
        return
    f2()
    print (locals())
    return
f1()
