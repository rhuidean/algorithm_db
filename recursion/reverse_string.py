def reverse(str):
	if len(str)==0:
		return ""

	return str[len(str)-1]+reverse(str[:len(str)-1])
		  
print reverse("d8xbsd")