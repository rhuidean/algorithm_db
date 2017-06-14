class BTNode(object):
	def __init__(self,value):
		self.val = value
		self.left = None
		self.right = None


class BST(object):
	def __init__(self):
		self.root = None

	def add(self,val,*current_node):
		print 'here', current_node
		### checking empty tuple
		if current_node == ():
			current_node = self.root
			print 'cn',  current_node

		new_node=BTNode(val)
		if self.root==None:
			self.root = new_node
			return

		current_node=self.root

		### While condition ~stop condition
		while current_node!=None:
				if current_node.val>=val:
					current_node=current_node.left
				else:
					current_node=current_node.right
				self.add(val,current_node)

			if current_node.val>=val:
				current_node.left=new_node

			else:
				current_node.right=new_node

		return self

b1=BST()
print b1.root
print b1.add(2)
print b1.root.val
print b1.root.right

print b1.add(3)
print b1.root.right.right
print b1.add(1)
print b1.root.left.val

b1.add(4)