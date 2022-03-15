// find continuous array where max and min present in an array

const findShortestArrLenMaxMin = (arr) =>{
    let max = -Infinity;
    let min = Infinity;
    for(let a of arr){
        if(max < a) max = a;
        if(min > a) min = a;
    }

    let n = arr.length;
    let len = Infinity;
    for(let i =0; i < n; i++){
        if(arr[i] == min){
            for(let j = i; j <n; j++){
                if(arr[j] == max){
                    len = Math.min(len, j-i+1);
                    break;
                }
            }
        }
        else if(arr[i] == max){
            for(let j = i; j < n; j++){
                if(arr[j] == min){
                    len = Math.min(len, j-i+1);
                    break;
                }
            }
        }
    }
    return len;
};

//optimized 

const optimizedCount = (arr)=>{
    let max = -Infinity;
    let min = Infinity;
    for(let a of arr){
        if(max < a) max = a;
        if(min > a) min = a;
    }

    let n = arr.length;
    let last_max = -1, last_min = -1, len = Infinity;
    for(let i = 0; i < n; i++){
        if(arr[i] == min) last_min = i;
        if(arr[i] == max) last_max = i;
        if(last_min != -1 && last_max !=-1)
            len = Math.min(len, Math.abs(last_max - last_min) +1);
    }
    return len;
}



// console.log(findShortestArrLenMaxMin([1,6,4,2,7,7,5,1,3,1,1,5]))

console.log(optimizedCount([1,6,4,2,7,7,5,1,3,1,1,5]))
