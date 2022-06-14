class HashTable{
    constructor(size){
        this.data = new Array(size);
    }

    _hash(key){
        let hash = 0;
        for(let i = 0; i < key.length; i++){
            hash = ( hash + key.charCodeAt(i) * i) % this.data.length;
        }
        return hash;
    }

    set(key, value){
        let index = this._hash(key);
        if(!this.data[index]){
            this.data[index] =[];
        }
        this.data[index].push([key,value]);
        return this.data;
    }

    get(key){
        let index = this._hash(key);
        if(this.data[index]){
            return this.data[index].find((valkey)=>  valkey[0] === key);
        }
        return null;
    }

    keys(){
        let keysArray = [];
        for(let i = 0; i< this.data.length; i++){
            if(this.data[i]){
                this.data[i].map((val)=>{
                    keysArray.push(val[0])
                });
            }
        }
        return keysArray;
    }
}

let hashTable = new HashTable(10);
hashTable.set('grapes', 1000);
hashTable.set('fruits', 90);



console.log(hashTable.set('vegetables', 60))

console.log(hashTable.get('fruit'))
console.log(hashTable.keys())