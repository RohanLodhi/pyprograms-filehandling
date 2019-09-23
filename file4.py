try:
	fp=open('data.txt','r')
	data=fp.read()
	print('File content :',data)
	fp.close()
except FileNotFoundError:
	print('File not found error')	

