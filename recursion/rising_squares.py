def rising_squares(num):
	import math 
		
	### start memoization
	if isinstance(num,int):
		print 1
		num={'array':[1],'num':num}
		return rising_squares(num)

	elif len(num['array'])==num['num']:
		return num['array']

	elif len(num['array'])<math.ceil(num['num']/2):
		last_index=len(num['array'])-1
		num['array'].append(math.pow(math.sqrt(num['array'][last_index])+2,2))
		# print num
		return rising_squares(num)

	elif len(num['array'])==math.ceil(num['num']/2):
		num['array'].append(math.pow(num['num'],2))
		return rising_squares(num)

	else:
		last_index=len(num['array'])-1
		num['array'].append(math.pow(math.sqrt(num['array'][last_index])-2*math.pow(0.5,math.sqrt(num['array'][last_index])%2),2))
		return rising_squares(num)
		
print "{}{}{}".format(rising_squares(1),rising_squares(7),rising_squares(2))