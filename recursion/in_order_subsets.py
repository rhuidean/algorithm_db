def string_order_subsets(str):
	### need to build recursion module error class
	array=[" ",1]
	current_grouping_size=len(str)

	if len(str)==0:
		return array

	elif current_grouping_size==0:
		return array

	else:
		for begin_index in range(len(str)-current_grouping_size):
			new_str=str[begin_index:begin_index+current_grouping_size]
			array.append(new_str)
		
		current_grouping_size-=1
		return string_order_subsets(str)
		

print string_order_subsets("abc")
		
	
	