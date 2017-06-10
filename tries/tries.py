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

# triset1=Triset()
# print "{} {} {}".format(triset1.root.key,triset1.root.value,triset1.root.children)

# triset1.root.key="a"
# print triset1.root


# string = "abc"

# print len(string[3:])