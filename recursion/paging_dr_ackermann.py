def ackermann(num1,num2):
	### need to build recursion module error class
	if num1==0 and num2>0 :
		return num2 + 1

	elif num1>0 and num2==0 :
		return ackermann(num1-1,1)

	else:
		return ackermann(num1-1,ackermann(num1,num2-1))

print ackermann(3,2)
