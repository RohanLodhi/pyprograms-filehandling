fp=open('data.txt','r')

print('file ptr position :',fp.tell())
data=fp.read(20)
print('File content :',data)
print('file ptr position :',fp.tell())

fp.seek(0)

data=fp.read(20)
print('File content :',data)
print('file ptr position :',fp.tell())	



fp.close()

