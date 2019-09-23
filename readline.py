with open("test.txt", "r") as f:
	pass

	##Small Files:
	'''
	f_contents = f.readline() 
	print(f_contents)

	f_contents = f.readline() 
	print(f_contents)	
	'''
	f_contents = f.readline() #return list
	print(f_contents,end='')

	f_contents = f.readline() #return list
	print(f_contents)	
	
print(f.closed)
