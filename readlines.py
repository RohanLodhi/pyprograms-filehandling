with open("test.txt", "r") as f:
	
	##Small Files:
	f_contents = f.readlines() #return list
	print(f_contents)
	
print(f.closed)
