def string_order_subsets(string):
	### need to build recursion module error class
	string_subset_list=[]
	
	if isinstance(string,str):
		string=[string[1:],string[0]]
		print string
		return string_order_subsets(string)

	elif len(string)==1:
		string_subset_list.append(string[0])
		return 1

	else:
		
		string1=[string[0][1:],string[1]]
		
		print string
		return string_order_subsets(string1)	
	# return string_subset_list

print string_order_subsets("abcd")

