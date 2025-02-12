#Write a Python program that can append the content of one file to another file.

file1=open('sample.txt','r')
file2=open('textfile.txt','r')

print("File 1 before merging is \n",file1.read())
print("File 2 before merging is \n",file2.read())

file1.close()
file2.close()

file1=open('sample.txt','a')
file2=open('textfile.txt','r')

file1.write(file2.read())



print("File 2 after merging is \n",file2.read())

file1.close()
file2.close()

