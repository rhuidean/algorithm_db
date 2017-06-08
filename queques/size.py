from queues import *
from isempty import *

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

SLQueue.size=size