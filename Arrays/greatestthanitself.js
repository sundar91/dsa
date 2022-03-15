const findCountGreaterThanItself = (arr)=>{
    let maxNumber = arr[0], maxCount = 0;
    for(let i = 1; i < arr.length; i++){
        if(maxNumber == arr[i]) maxCount++;
        if(maxNumber < arr[i]){
            maxNumber = arr[i];
            maxCount = 1;
        }
    }
    return arr.length - maxCount;
}

var count = findCountGreaterThanItself([2,5,1,4,8,0,8,1,3,8]);
console.log(count);
