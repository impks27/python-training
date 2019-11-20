#Modifying text files. Upper case first 15 chars of txt file
import os,sys
os.system ('cls')

with open('testfile.txt','r+') as fo:
    print ('The byte no @begin is ', fo.tell())
    s=fo.read(15)
    print ('The byte no. after 15chars is: ', fo.tell())
    t=s.upper()
    fo.seek(0,0)
    print ('The byte no. after reposition is ', fo.tell())
    fo.write(t)
