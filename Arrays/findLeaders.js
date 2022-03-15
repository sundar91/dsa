const findLeaders = (arr) => {
    let n = arr.length;
    let count = 1, max = arr[n-1]
    for(let i = n - 2; i >= 0; i--){
        if(arr[i] > max){
            count++;
            max = arr[i];
        }
    }
    return count;
}

console.log(findLeaders([16,17,17,4,3,5,2]))