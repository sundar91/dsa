class Node{
    constructor(value){
        this.value = value;
        this.next = null;
    }
}

class Queue{
    constructor(){
        this.first = null;
        this.last = null;
        this.length = 0 ;
    }

    peek(){
        return this.first;
    }

    enqueue(value){
        let newNode = new Node(value);
        if(this.length ===0){
            this.first = newNode;
            this.last = newNode;
        }
        else{
            this.last.next = newNode;
            this.last = newNode;
        }
        this.length++;
        return this;
    }

    dequeue(){
        if(this.length === 0) return null;
        if(this.first === null) this.last = null;

        this.first = this.first.next;
        this.length--;
        return this;
    }
}

const myQueue = new Queue();
myQueue.enqueue('John');
myQueue.enqueue('Matt');
myQueue.enqueue('Jackson');
myQueue.enqueue('Lauren');

myQueue.dequeue();

console.log(myQueue);