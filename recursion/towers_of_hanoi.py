def towers_of_hanoi(num):
	import math 
		
	### start memoization
	if isinstance(num,int):
		list_a = [number for number in reversed(range(1,num+1))]
		list_b = []
		list_c = []
		num = {"list_a":list_a,"list_b":list_b,"list_c":list_c}
		print num['list_a']
		print num['list_b']
		print num['list_c']
		print "-"*30
		return towers_of_hanoi(num)

	elif len(num["list_c"])==0:
		num["list_c"].append(num['list_a'].pop())
		print num['list_a']
		print num['list_b']
		print num['list_c']
		print "-"*30
		return towers_of_hanoi(num)

	elif len(num["list_b"])==0:
		num["list_b"].append(num['list_a'].pop())
		print num['list_a']
		print num['list_b']
		print num['list_c']
		print "-"*30
		return towers_of_hanoi(num)

		


print towers_of_hanoi(9)
