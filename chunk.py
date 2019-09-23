with open("test.txt", "r") as f:
	###Going Back....:	
	#f_contents = f.read()
	#print(f_contents, end = '')
	'''
	###Printing by characters:
	f_contents = f.read(100)
	print(f_contents, end = '')
	f_contents = f.read(100)
	print(f_contents, end = '')
	f_contents = f.read(100)
	print(f_contents, end = '')
	'''
	'''
	###Iterating through small chunks:
	size_to_read = 100
	f_contents = f.read(size_to_read)
	while len(f_contents) > 0:
		print(f_contents)
		f_contents = f.read(size_to_read)
	'''
	
	###Iterating through small chunks, with 10 characters:
	size_to_read = 10
	f_contents = f.read(size_to_read)
	print(f_contents, end = '')
	f.seek(0)
	f_contents = f.read(size_to_read)
	print(f_contents, end = '')
	
	print(f.tell())
	while len(f_contents) > 0:
		print(f_contents, end = '')
		f_contents = f.read(size_to_read)
	
print()
print(f.mode)
print(f.closed)

