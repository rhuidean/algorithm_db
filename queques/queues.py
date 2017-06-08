class SLNode(object):
	'''Node Object'''
	def __init__(self, value):
		self.val = value
		self.next = None


class SLQueue(object):
	def __init__(self):
		self.head = None
		self.tail = None

