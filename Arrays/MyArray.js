class MyArray{
    constructor(){
        this.data = {};
        this.length = 0;
    } 

    get(index){
        return this.data[index];
   }

   push(value){
      this.data[this.length] = value;
      this.length++;
   }
   
   pop(){
     const lastItem = this.data[this.length - 1];
     delete this.data[this.length -1]
     this.length--;
     return lastItem;
   }

   delete(index){
       delete this.data[index];
        this.shiftItems(index);
   }

   shiftItems(index){
        for(let i = index; i < this.length - 1; i++){
            this.data[i] = this.data[i+1]
        }
        delete this.data[this.length - 1] ;
        this.length--;
   }

}