fp=open('data.txt','w')

print('file name :',fp.name)
print('file mode :',fp.mode)
print('file close :',fp.closed)

fp.close()

print('file close :',fp.closed)

