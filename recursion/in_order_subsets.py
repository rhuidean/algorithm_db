def string_order_subsets(string):
	### need to build recursion module error class
		
	if isinstance(string,str):
		string=[string[1:],string[0]]
		print string
		return string_order_subsets(string)

	elif string[0]=='':
		
		print string
		return string[1]+" "

	else:
		string0=[string[0][1:],string[1]+string[0][0]]
		string1=[string[0][1:],string[1]]
		
		# print string0
		# print string1
		return string_order_subsets(string0)+string_order_subsets(string1)	
	

print string_order_subsets("abcd")

