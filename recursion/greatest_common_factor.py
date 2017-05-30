import math
def gbc(num1,num2):
	### need to build recursion module error class
	
	if (num1%num2)*(num2%num1)==0:
		return min(num1,num2)

	elif num1 > num2:
		return gbc(num1%num2,num2)
		# return gbc(num1-num2,num2)

	else:
		return gbc(num1,num2%num1)
		# return gbc(num1,num2-num1)

print gbc(123456,987654)
	
	