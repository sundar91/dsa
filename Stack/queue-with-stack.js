class Queue{
    constructor(){
        this.first =[];
        this.last = [];
    }

    peek(){
        if(this.last.length > 0) return this.last[0];

        return this.first[this.first.length - 1];
    }

    push(value){
        const length = this.first.length;
        for(let i =0; i < length; i++){
            this.last.push(this.first.pop());
        }
        this.last.push(value);
        return this;
    }

    pop(){
       let length = this.last.length;
       for(let i = 0; i < length; i++){
           this.first.push(this.last.pop());
       }
       this.first.pop();
       return this;
    }
}

const myQueue = new Queue();
myQueue.push(1);
myQueue.push(2);

console.log(myQueue.pop());

console.log(myQueue.peek())