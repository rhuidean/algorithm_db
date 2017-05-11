
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

LinkedList.prototype.Display = function(){
	var str = "";
	var runner = this.head;

	if(this.head == null){
		console.log('linked list is empty')
	}
	while(runner){
		str = str + runner.val+',';
		runner = runner.next
	}
	console.log(str)
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

LinkedList.prototype.addBack = function(val){
	var runner = this.head;
	var new_node = new Node(val)
	if(this.head == null){
		this.head = new_node;
	}

	while(runner){
		if(runner.next == null){
			runner.next = new_node;
			break
		}
		runner = runner.next;
	}
}

var list = new LinkedList()
//test case
list.addFront(7);
list.addFront(5);
list.addFront(10);
list.addFront(1);
list.addBack(-3)
list.Display()
list.addBack(3)
list.Display()


