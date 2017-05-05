

function Node(val){
	this.val = val;
	this.next = null;
}

function LinkedList(){
	this.head = null;
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

//test case
//create a new linked list
var list = new LinkedList()
list.addFront(5);
list.addFront(10);
list.addFront(1);
console.log(list)



