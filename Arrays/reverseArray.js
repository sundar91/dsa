const reverseArray = (arr) =>{
    let n = arr.length;
    for(let i = 0, j = n - 1; i < j; i++, j--){
        let temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    return arr;
}

console.log(reverseArray([2,5,1,4,8]));