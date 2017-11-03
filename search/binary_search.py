def binary_search(arr, val):
	value = val

	if len(arr)==1:
		if arr[0]==val:
			return True
		else:
			return False

	arr.sort()

	low_point_idx = 0
	mid_point_idx = len(arr)/2
	high_point_idx = len(arr)-1

	if arr[mid_point_idx]== val:
		return True

	elif arr[mid_point_idx] < val:
		arr=arr[mid_point_idx:]
		return binary_search(arr,value)

	else :
		arr=arr[:mid_point_idx]
		return binary_search(arr,value)


print binary_search([3,1,2,5],1)