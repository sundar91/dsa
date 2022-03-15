class Node {
    constructor(value){
        this.value = value;
        this.next = null;
    }
}

class Stack {
    constructor(){
        this.top = null;
        this.bottom = null;
        this.length = 0;
    }

    peek(){
        return this.top;
    }
    push(value){
        let newNode = new Node(value);
        if(this.bottom === null){
            this.top = newNode;
            this.bottom = newNode;
        }
        else{
            newNode.next = this.top;
            this.top  = newNode;
        }
        this.length++;
        return this;
    }
    pop(){
        if(this.top === null) return null;

        let node = this.top;
        this.top = this.top.next;
        if(this.top === null) this.bottom = null;
        this.length--;
        return node;
    }
}

const myStack = new Stack();
myStack.push(20);
myStack.push(30);

console.log(myStack);
myStack.pop();

console.log(myStack.peek());