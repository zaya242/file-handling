file_read=open('textfile.txt','r')
print(file_read.read())
file_read.close()


file_write=open('textfile.txt','w')
file_write.write("my name is zainab and i am 16")
file_write.close()


file_append=open('textfile.txt','a')
file_append.write("\nI am zainab an i live in abuja")
file_append.close()
