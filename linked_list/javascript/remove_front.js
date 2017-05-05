

function Node(val){
	this.val = val;
	this.next = null;
}

function LinkedList(){
	this.head = null;
}

LinkedList.prototype.removeFront = function(){
	if (this.head == null){
		return this;
	}
	else if (this.head.next == null){
		this.head = null;
	}
	else{
		this.head = this.head.next;
	}
}

LinkedList.prototype.addFront = function(val){
	//creating a new node
	var new_node = new Node(val);

	//if the list is empty
	if(this.head == null){
		this.head = new_node;
	}
	//if the list is not empty
	else{
		new_node.next = this.head;
		this.head = new_node;
	}

	return this;
}


var list = new LinkedList()
//test case
list.addFront(5);
list.addFront(10);
list.addFront(1);
console.log(list)
list.removeFront()
console.log(list)
list.removeFront()
console.log(list)

