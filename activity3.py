
#Write a Python program that can calculate and return the total number of lines present inside a file. First, you would be required to read the contents of the file.

file=open('textfile.txt','r')
content=file.read()
colist=content.split("\n")
count=0

for i in colist:
    if i:
        count+=1

print("Number of lines in the file is",count)        