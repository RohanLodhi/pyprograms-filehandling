fp=open('data.txt','r')

data=fp.read()
print('File content :',data)

#data=fp.read(100)
#print('File content :',data)

fp.close()

