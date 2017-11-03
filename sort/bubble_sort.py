def bubble_sort(arr):
	for loop_index in range(len(arr)-1):
		for sorting_index in range(len(arr)-1):
			if arr[sorting_index] > arr[sorting_index+1]:
				arr[sorting_index],arr[sorting_index+1] = arr[sorting_index+1],arr[sorting_index]

	return arr

print bubble_sort([5,3,7,9,1,10])
print len([1,3])