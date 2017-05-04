class ListNode(object):
	'''Node Object'''
	def __init__(self, value):
		self.val = value
		self.next = None

b = ListNode(4)

# print "{} {} {}".format(b,b.val,b.next)


class LinkedList():
	def __init__(self):
		self.head = None

	def addFront(self,value):
		new_node = ListNode(value)
		if self.head == None:
			self.head = new_node

		else:
			new_node.next = self.head
			self.head = new_node

		return self

	def contains(self,value):
		pointer = self.head
		while pointer != None:
			if pointer.val == value:
				return True
			pointer = pointer.next
		return False

	def removeFront(self):
		if self.head == None:
			return None
		elif self.head.next == None:
			return None
		else:
			self.head = self.head.next 
			return self

	def front(self):
		if self.head == None:
			return None
		else:
			return self.head.val

	def length(self):
		count = 0
		if self.head == None:
			return count
		else:
			pointer = self.head
			while pointer != None:
				count +=1
				pointer = pointer.next
		return count

	def display(self):
		mylist = []
		if self.head == None:
			print None

		else:
			pointer = self.head
			
			while pointer != None:
				mylist.append(pointer)
				pointer = pointer.next
			print "{}".format(" ".join(mylist))


	def max(self):
		if self.head == None:
			print None

		max = self.head	
		pointer = self.head

		while pointer.next!= None:
			if max < pointer:
				max = pointer

		return self


	def min(self):	
		if self.head == None:
			print None

		min = self.head	
		pointer = self.head

		while pointer.next!= None:
			if min > pointer:
				min = pointer

		return self





# a = ListNode(3)
# print "{} {}".format(a.val,a.next)

# b = LinkedList()
# # b.addFront(3)
# # print "{} {} {}".format(b,b.head.val,b.head.next)

# print b.addFront(3)
# print b.contains(3)

# b.removeFront()
# print b.length()


