def collatz(num):
	print num
	if num==1:
		return

	elif num%2==0:
		num=num/2
		return collatz(num)
	
	else:
		num = num*3+1
		return collatz(num)

print collatz(5)