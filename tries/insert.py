from tries import *

def insert(self,string):
	### save initial string & start traversing from the root node
	original_string = string
	current_node = self.root

	### create a key and a new subset string
	current_character=string[0]
	string=string[1:]

	### check if original string is already in the tries instance 
	### if it does not exist in the root's children list
	### then create a new node and include it in the list
	if current_character not in current_node.children.keys():
		while len(string) > 0:
			new_node=TrieNode()
			new_node.key=current_character
			### Adding value to the node case: check if current_character is the last character in the original string 
			if len(string) == 0:
				new_node.value=original_string
			current_node.children[current_character]=new_node
			if len(string) == 0:
				return self
			
			### loop through characters of new subset strings
			current_node=current_node.children[current_character]
			current_character=string[0]
			string=string[1:]

	# ### otherwise go to one of root's children keys that is equal to the current character i.e. the first character of the original string.
	# else:
	# 	current_node=current_node.children[current_character]

	# 	### loop through the pre-inserted string's characters and insert new characters that does not exist.
	# 	while len(string) > 0:
	# 		current_character=string[0]
	# 		string=string[1:]
	# 		if current_character not in current_node.children.keys():
	# 			new_node=TrieNode()
	# 			new_node.key=current_character
	# 			### Adding value to the node case: check if current_character is the last character in the original string 
	# 			if len(string) == 0:
	# 				new_node.value=original_string
	# 			current_node.children[key]=new_node
	# 			if len(string) == 0:
	# 				return self

	# 			current_node=current_node.children[current_character]

		

Triset.insert=insert
	
triset1=Triset()
triset1.insert("Jason")
print "{} {} {}".format(triset1.root.key,triset1.root.value,triset1.root.children)

print triset1.root.children['J']

children1=triset1.root.children['J']
print children1.children
for key in children1.children.keys():
	print key

children2=children1.children['a']
print children2.children
print children2

def print_iterables(node):
	if len(node.children.keys())==0:
		return

	for key in node.children.keys():
		print node.children[key]
		node=node.children[key]
		
	return print_iterables(node)

print_iterables(triset1.root)

