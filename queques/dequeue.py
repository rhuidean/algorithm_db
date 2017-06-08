from queues import *
from isempty import *

def dequeue(self):
	if self.isEmpty():
		return None

	else:
		front_node = self.head
		self.head = self.head.next
		front_node.next = None
		return front_node.val

SLQueue.dequeue=dequeue