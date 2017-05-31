def string_order_subsets(string):
	### need to build recursion module error class
	string_subset_list=[]
	
	if isinstance(string,str):
		string=[string[1:],string[0]]
		return string_order_subsets(string)

	elif len(string)==1:
		string_subset_list.append(string[0])

	else:
		string0=[string[0][1:],string[1]+string[0][0]]
		string1=[string[0][1:],string[1]]
		new_string_list=[string0,string1]
		for string in new_string_list:
			return string_order_subsets(string)	
	# return string_subset_list

print string_order_subsets("abcd")

string1=['cd','ab']
string2=[string1[0][1:],string1[1]+string1[0][0]]
print string2