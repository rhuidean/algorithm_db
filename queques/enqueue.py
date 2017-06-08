from queues import *
from isempty import *

def enqueue(self,value):
	new_node = SLNode(value)
	if self.isEmpty():
		self.head = new_node
		self.tail = new_node

	else:
		self.tail.next = new_node
		self.tail = new_node

	return self

SLQueue.enqueue=enqueue