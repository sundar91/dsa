const firstRecurringNumber = (numbers)=>{
    const keys = {}
    for(let num of numbers){
        if(keys[num])
            return num;
        
        keys[num] = true;
    }
    return null;
}

console.log(firstRecurringNumber([2,4,5,6,7,8,9,7,51]))