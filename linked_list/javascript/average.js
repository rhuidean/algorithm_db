
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

LinkedList.prototype.Length = function(){
	runner = this.head;
	count = 0;

	while(runner){
		count++;
		runner = runner.next;
	}
	return count;
}

LinkedList.prototype.average = function(){
	var runner = this.head;
	var sum = 0;
	var avg = 0;

	while(runner){
		sum += runner.val;
		runner = runner.next;
	}
	return sum/this.Length()
	
}

var list = new LinkedList()
//test case
list.addFront(5);
list.addFront(10);
list.addFront(1);
console.log(list.average())


