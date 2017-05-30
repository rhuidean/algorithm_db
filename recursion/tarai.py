def tarai(x,y,z):
	### need to build recursion module error class
	if x < y :
		return y

	else:
		return tarai(tarai(x-1,y,z),tarai(y-1,z,x),tarai(z-1,x,y))

print tarai(10,2,9)
