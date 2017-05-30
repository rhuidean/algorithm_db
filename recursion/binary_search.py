import math
def rBinarySearch(array,num):
	### need to build recursion module error class
	mid_point = int(math.floor(len(array)/2))
	
	if len(array)==1 and array[0]!=num:
		return False

	elif array[mid_point] > num:
		new_array = array[:mid_point]
		return rBinarySearch(new_array,num)

	elif array[mid_point] < num:
		new_array = array[mid_point:]
		return rBinarySearch(new_array,num)

	else:
		return True
		
print rBinarySearch([1,2,3],1)
print rBinarySearch([1,2,3],3)
print rBinarySearch([1,2,3],0)
