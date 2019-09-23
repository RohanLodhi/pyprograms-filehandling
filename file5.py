fp=open('data.txt','r')

print('file ptr position :',fp.tell())

data=fp.read()
print('File content :',data)

print('file ptr position :',fp.tell())



fp.close()

