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

	
