class BTNode(object):
	def __init__(self,value):
		self.val = value
		self.left = None
		self.right = None


class BST(object):
	def __init__(self):
		self.root = None

	def add(self,val):	
		if self.root==None:
			self.root=BTNode(val)
			return 

		current_node=self.root
		new_node=BTNode(val)

		### While condition ~stop condition
		### Extra cautious in while loop. Check the return conditions
		while current_node!=None:
			if current_node.val>=val:
				if current_node.left==None:
					current_node.left=new_node
					return

				elif current_node.val==new_node.val:
						shift_node=current_node.left
						new_node.left=shift_node
						current_node.left=new_node
						return
				else:
					print "new",new_node.val
					print "curr",current_node.val
					current_node=current_node.left
			
			else:
				if current_node.right==None:
					current_node.right=new_node
					return

				elif current_node.val==new_node.val: 
					shift_node==current_node.right
					new_node.right=shift_node
					current_node.right=new_node
					return
				else:
					current_node=current_node.right

	def contains(self,val):
		current_node=self.root

		while current_node!=None:
			if current_node.val==val:
				return True

			else:
				if current_node.val > val:
					current_node=current_node.left

				else:
					current_node=current_node.right
		return False

	def min(self):
		current_node=self.root

		while current_node.left!=None:
			current_node=current_node.left

		return current_node.val

	def max(self):
		current_node=self.root

		while current_node.right!=None:
			current_node=current_node.right

		return current_node.val
			

b1=BST()
print b1.root
b1.add(2)
print b1.root.val
b1.add(1)
b1.add(3)
print b1.root.right.val
print b1.root.left.val
b1.add(2)
print b1.root.left.val
print b1.root.left.left.val

print b1.contains(7)
print b1.min()
print b1.max()