#recursion. It uses stack hence reverse
def mlt(n,l):
    if l<1:
        return
    else:
        mlt(n,l-1)
        print ('%d * %d = %d' % (n,l,n*l))

mlt(10,12)
