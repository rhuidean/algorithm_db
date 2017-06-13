### Create TriesNode object containing optional node value and array of pointers
class TrieNode(object):
	### declare attributes
	def __init__(self):
		### by default node's value is an empty string
		self.key = None
		self.value = None
		self.children = {}


### Create Triset object 
class Triset(object):
	### declared above the __init__ becomes attribute
	new_node=TrieNode()
	new_node.key=""

	def __init__(self):
		self.root = self.new_node

	def insert(self,string):
		original_string = string
		current_node = self.root 

		current_character=string[0]
		string=string[1:]

		if current_character not in self.root.children.keys():
			while len(string) >= 0:
				new_node=TrieNode()
				new_node.key=current_character
				### Adding value to the node case: check if current_character is the last character in the original string 
				if len(string) == 0:
					new_node.value=original_string
				current_node.children[current_character]=new_node
				if len(string) == 0:
					return self
				
				## loop through characters of new subset strings
				current_node=current_node.children[current_character]
				current_character=string[0]
				string=string[1:]

		
		## otherwise go to one of root's children keys that is equal to the current character i.e. the first character of the original string.
		else:

			current_node=current_node.children[current_character]

			### loop through the pre-inserted string's characters and insert new characters that does not exist.
			while len(string) > 0:
				current_character=string[0]
				string=string[1:]

				if current_character not in current_node.children.keys():
					new_node=TrieNode()
					new_node.key=current_character
					### Adding value to the node case: check if current_character is the last character in the original string 
					if len(string) == 0 and current_node.value!=original_string:
						new_node.value=original_string
					current_node.children[current_character]=new_node
					return self

				elif len(string) == 0:
					return self

				current_node=current_node.children[current_character]

	
	def contains(self,string):
		current_node=self.root
		current_character=string[0]
		string=string[1:]

		### check if current character is in current_node's children dictionary
		while current_character in current_node.children.keys():
			### loop through and check next character in the string
			current_node=current_node.children[current_character]
			current_character=string[0]
			string=string[1:]
			if len(string)==0 and current_character in current_node.children.keys():
				return True

		return False		

	def first(self):
		### create an empty first_value list
		first_value=[]
		current_node=self.root

		### loop through pre-inserted characters and retrieve first characters of each alphabetically sorted characters.
		while current_node.children.keys():
			current_character=[key for key in sorted(current_node.children.keys())][0]
			first_value.append(current_character)
			current_node=current_node.children[current_character]
			if current_node.value:
				return ''.join(first_value)
		
	def last(self):
		### create an empty last_value list
		last_value=[]
		current_node=self.root

		### loop through pre-inserted characters and retrieve first characters of each alphabetically reverse sorted characters.
		while current_node.children.keys():
			current_character=[key for key in sorted(current_node.children.keys(),reverse=True)][0]
			last_value.append(current_character)
			current_node=current_node.children[current_character]
			if not current_node.children:
				return ''.join(last_value)

	def test(self, n):
		if n == 0:
			return
		print 'testing'
		self.test(n - 1)

	def size(self,current_node,count=0):
		### loop through all the character nodes and count the number of node values.

		if len(current_node.children)==0:
			return count

		for key in current_node.children.keys():
			if current_node.children[key].value!=None:
				count +=1
			print count
			print key

			child_node=current_node.children[key]
			print 'CHILD NODE:', child_node.value
			
			self.size(child_node,count)

# 	# def display(self):
# 	# 	if self.root.children.keys():
# 	# 		node = self.root
# 	# 		if node.children.keys()==None:
# 	# 			return self
	
# 	# 		for key in node.children.keys():
# 	# 			print node.children[key].key
# 	# 			node =node.children[key]
# 	# 			return display(self.node)

# 		# else:
# 		# 	print "No strings has been set."
# 		# 	return self

T1=Triset()
T1.test(3)
T1.insert('Jason')

print T1.root.children['J'].children['a'].children['s'].children['o'].children
T1.insert('JasonM')

print T1.root.children['J'].children['a'].children['s'].children['o'].children['n'].children

T1.insert('Bat').insert('BatY')
print T1.root.children

print T1.contains('JasonM')
print T1.root.children["B"].children['a'].children['t'].key
string="XYX"
print string.endswith("X")

print T1.first()
print T1.last()

print T1.size(T1.root)
# print len(T1.root.children)
# print T1.size(T1.root)
# print T1.root.children
# print T1.root.children['B'].value

# print "XYA"[-1]