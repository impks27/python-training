with open('testfile.txt','r') as fo:
    print ('the name of the file is ', fo.name)
    print ('the mode of the file is ', fo.mode)
    print ('the filemis closed ', fo.closed) #False
print ('the filemis closed ', fo.closed) #True
