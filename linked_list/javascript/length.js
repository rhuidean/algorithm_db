
function Node(val){
	this.val = val;
	this.next = null;
}

function LinkedList(){
	this.head = null;
}

LinkedList.prototype.Length = function(){
	runner = this.head;
	count = 0;

	while(runner){
		count++;
		runner = runner.next;
	}
	return count;
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
console.log(list)
//checking before add any node into linked list
console.log(list.Length())
list.addFront(5);
list.addFront(10);
list.addFront(1);
//checking before add any node into linked list
console.log(list.Length())

