class SLNode(object):
	'''Node Object'''
	def __init__(self, value):
		self.val = value
		self.next = None


class SLQueue(object):
	### *args
	def __init__(self,*args):
		self.head = None
		self.tail = None

		for arg in args:
			self.enqueue(arg)

	def isEmpty(self):
		if self.head == None:
			return True

	def enqueue(self,value):
		new_node = SLNode(value)
		if self.isEmpty():
			self.head = new_node
			self.tail = new_node

		else:
			self.tail.next = new_node
			self.tail = new_node

		return self

# a=SLQueue(1,4,5,6)
# print a.head.val


	

