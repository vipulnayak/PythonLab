import os.path
import sys
fname=input("enter the file name \n")
if not os.path.isfile(fname):
    print("the entered file does not exist")
    sys.exit(0)

infile=open(fname,'r')
linelist=infile.readlines()
for i in range(len(linelist)):
    print(i+1,":",linelist[i],end=" ")
count=0
word=input(" \n enter the word to be counted \n")
for line in linelist:
    count+=line.count(word)
print("the word",word,"appears",count,"times in the file")
