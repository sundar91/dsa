class Node{
    constructor(value){
        this.value = value;
        this.next = null;
    }
}

class LinkedList{
    constructor(value){
        this.head = {
            value : value,
            next: null
        };
        this.tail = this.head;
        this.length = 1;
    }

    append(value){
        let newNode = new Node(value);

        this.tail.next = newNode;
        this.tail= newNode;
        this.length++;
        return this;
    }

    prepend(value){
        let newNode =  new Node(value);
        newNode.next = this.head;

        this.head = newNode;
        this.length++;
        return this;
    }

    printList(){
        const array = [];
        let currentNode = this.head
        while(currentNode){
            array.push(currentNode.value);
            currentNode = currentNode.next;
        }
        return array;
    }
    insert(index, value){
        

        if(index==0){
            this.prepend(value);
            return this.printList();
        }

        if(index >= this.length){
            this.append(value);
            return this.printList();
        }

       let currentNode = this.traverseToIndex(index-1);

        if(currentNode){
            let newNode = new Node(value);
            
            newNode.next = currentNode.next;
            currentNode.next = newNode;
        }

        this.length++;
        return this;

    } 

    traverseToIndex(index){
        let currentIndex = 0,
            currentNode = this.head;

        while(currentIndex !== index && currentNode){
            currentNode = currentNode.next;
            currentIndex++;
        } 
        return currentNode;
    }

    remove(index){
        if(index === 0){
            this.head = this.head.next;
            this.length--;
        }

        let node = this.traverseToIndex(index - 1);
        if(node){
            node.next = node.next.next;
            this.length--;
        }
        return this.printList();
    }

    reverse(){
        if(!this.head.next){
            return this;
        }

        let first = this.head;
        this.tail = this.head;
        let second = this.head.next;
        while(second){
            const temp = second.next;
            second.next = first;
            first = second;
            second = temp;
        }
        this.head.next = null; // clearing null of the first element
        this.head = first; 
    }

}

const myLinkedList = new LinkedList(10);
myLinkedList.append(5);
myLinkedList.append(16);

myLinkedList.prepend(7);

myLinkedList.insert(2,8);
console.log(myLinkedList.printList());

myLinkedList.remove(3);

console.log(myLinkedList.printList());
myLinkedList.reverse();
console.log(myLinkedList.printList());