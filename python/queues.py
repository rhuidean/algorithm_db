class SLNode(object):
	'''Node Object'''
	def __init__(self, value):
		self.val = value
		self.next = None


class SLQueue(object):
	def __init__(self):
		self.head = None
		self.tail = None

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

	def dequeue(self):
		if self.isEmpty():
			return None

		else:
			front_node = self.head
			self.head = self.head.next
			front_node.next = None
			return front_node.val

	def size(self):
		if self.isEmpty():
			return 0

		else:
			start_pointer = self.head
			self.enqueue(self.dequeue())
			size = 1
			start_pointer = start_pointer.next
			while start_pointer:
				self.enqueue(self.dequeue())
				size += 1
				start_pointer = start_pointer.next

		return size

		
a = SLNode(1)

b = SLQueue()
b.enqueue(1).enqueue(5).enqueue(7)
b.enqueue(b.dequeue())
print "{},{}".format(b.head.val , b.tail.val)

print b.size()
