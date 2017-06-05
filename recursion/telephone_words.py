def telephone_words(string):
	### need to build recursion module error class
	
	### create string object with array and original string numbers5	
	if isinstance(string,str):
		string={'array':"",'string':string}
		# return string
		return telephone_words(string)

	elif len(string['string'])==0:
		print string['array']
		return string['array']+" "

	else:
		if string['string'][0] == '2':
			string0={'array':string['array']+'a','string':string['string'][1:]}
			string1={'array':string['array']+'b','string':string['string'][1:]}
			string2={'array':string['array']+'c','string':string['string'][1:]}
			return telephone_words(string0)+telephone_words(string1)+telephone_words(string2)

		elif string['string'][0] == '3':
			string0={'array':string['array']+'d','string':string['string'][1:]}
			string1={'array':string['array']+'e','string':string['string'][1:]}
			string2={'array':string['array']+'f','string':string['string'][1:]}
			return telephone_words(string0)+telephone_words(string1)+telephone_words(string2)

		elif string['string'][0] == '4':
			string0={'array':string['array']+'g','string':string['string'][1:]}
			string1={'array':string['array']+'h','string':string['string'][1:]}
			string2={'array':string['array']+'i','string':string['string'][1:]}
			return telephone_words(string0)+telephone_words(string1)+telephone_words(string2)

		elif string['string'][0] == '5':
			string0={'array':string['array']+'j','string':string['string'][1:]}
			string1={'array':string['array']+'k','string':string['string'][1:]}
			string2={'array':string['array']+'l','string':string['string'][1:]}
			return telephone_words(string0)+telephone_words(string1)+telephone_words(string2)

		elif string['string'][0] == '6':
			string0={'array':string['array']+'m','string':string['string'][1:]}
			string1={'array':string['array']+'n','string':string['string'][1:]}
			string2={'array':string['array']+'o','string':string['string'][1:]}
			return telephone_words(string0)+telephone_words(string1)+telephone_words(string2)

		elif string['string'][0] == '7':
			string0={'array':string['array']+'p','string':string['string'][1:]}
			string1={'array':string['array']+'q','string':string['string'][1:]}
			string2={'array':string['array']+'r','string':string['string'][1:]}
			string3={'array':string['array']+'s','string':string['string'][1:]}
			return telephone_words(string0)+telephone_words(string1)+telephone_words(string2)+telephone_words(string3)

		elif string['string'][0] == '8':
			string0={'array':string['array']+'t','string':string['string'][1:]}
			string1={'array':string['array']+'u','string':string['string'][1:]}
			string2={'array':string['array']+'v','string':string['string'][1:]}
			return telephone_words(string0)+telephone_words(string1)+telephone_words(string2)

		elif string['string'][0] == '9':
			string0={'array':string['array']+'w','string':string['string'][1:]}
			string1={'array':string['array']+'x','string':string['string'][1:]}
			string2={'array':string['array']+'y','string':string['string'][1:]}
			string3={'array':string['array']+'z','string':string['string'][1:]}
			return telephone_words(string0)+telephone_words(string1)+telephone_words(string2)+telephone_words(string3)

		elif string['string'][0] == '1':
			string0={'array':string['array']+'i','string':string['string'][1:]}
			return telephone_words(string0)

		elif string['string'][0] == '0':
			string0={'array':string['array']+'o','string':string['string'][1:]}
			return telephone_words(string0)

		else:
			string0={'array':string['array'],'string':string['string'][1:]}
			return telephone_words(string0)


print telephone_words('204-5083')
