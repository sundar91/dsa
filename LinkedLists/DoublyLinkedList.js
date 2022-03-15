class Node {
    constructor(value){
        this.value =value;
        this.next = null;
        this.prev = null;
    }
}

class LinkedList{
    constructor(value){
        this.head = new Node(value);
        this.length = 1;
        this.tail = this.head;
    }

    append(value){
        let newNode = new Node(value);
        this.tail.next  = newNode;
        newNode.prev = this.tail;
        this.tail = newNode;
        this.length++;
        return this;
    }

    prepend(value){
        let newNode = new Node(value);
        newNode.next = this.head;
        this.head.prev = newNode;
        this.head = newNode;
        this.length++;
        return this;
    }

    printList(){
        let traverseArray = [];
        let currentNode = this.head;
        while(currentNode){
            traverseArray.push(currentNode.value);
            currentNode = currentNode.next;
        }
        return traverseArray;
    }

    insert(index, value){
        if(index === 0){
            return this.prepend(value);
        }

        if(index >= this.length){
            return this.append(value);
        }

        let leader = this.traverseToIndex(index-1);
        let newNode = new Node(value);
        newNode.prev = leader;
        newNode.next = leader.next;
       
        leader.next.prev = newNode;
        leader.next = newNode;

        this.length++;
        return this.printList();
    }

    remove(index){
        if(index === 0){
            this.head.next.prev = null; 
            this.head = this.head.next;
            this.length--;
            return this;
        }

        let leader = this.traverseToIndex(index-1);
        let follower = leader.next?.next;
        leader.next = follower;
        if(follower != null){
            follower.prev = leader;
        }
        else{
            this.tail = leader;
        }
        this.length--;
        return this;
        

    }

    traverseToIndex(index){
        let currentIndex = 0,
        currentNode = this.head;

        while( currentIndex !== index){
            currentNode = currentNode.next;
            currentIndex++;
        }
        return currentNode;
    }
}

const myLinkedList = new LinkedList(10);

myLinkedList.append(20);
myLinkedList.append(30);

myLinkedList.prepend(5);

myLinkedList.insert(2,25);

console.log(myLinkedList.printList());
myLinkedList.remove(2);

console.log(myLinkedList.printList());

myLinkedList.remove(3);

console.log(myLinkedList.printList());
console.log(myLinkedList);