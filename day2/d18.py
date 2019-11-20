#copying of the file using command line.
#python d18.py testfile.txt testfile1.txt
import os,sys
os.system ('cls')

with open(sys.argv[1],'r') as fo1, open(sys.argv[2],'w') as fo2:
    s=fo1.read()
    fo2.write(s)
    
