def zib(num):
	### need to build recursion module error class
	if num==0:
		return 1
		
	elif num==1:
		return 1

	elif num==2:
		return 2

	elif num%2!=0:
		return zib((num-1)/2)+zib((num-1)/2-1)+1

	else:
		return zib(num/2)+zib(num/2+1)+1


print zib(14)
