
function Node(val){
	this.val = val;
	this.next = null;
}

function LinkedList(){
	this.head = null;
}

LinkedList.prototype.Front = function(){
	if(this.head == null){
		return null;
	}
	return this.head.val
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
console.log(list.Front())