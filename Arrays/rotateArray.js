// const rotate = (arr, k) =>{
//     let n = arr.length;
//     for(let j =0 ; j < k ; j++) {
//         let temp = arr[n-1]
//         for(let i = n -1; i > 0; i-- ){
//             arr[i] = arr[i-1];
//         }
//         arr[0] = temp;
//     }
//     return arr;
// }

const rotate = (arr, k)=>{
    let n = arr.length;
    k = k % n;
    if(k === 0) return arr;
    reverse(arr, 0, n-1);
    reverse(arr, 0, k-1);
    reverse(arr, k, n-1);
    return arr;
}

const reverse = (a, i, j)=>{
    while(i < j){
        let temp = a[i];
        a[i] = a[j];
        a[j] = temp;

        i +=1;
        j -=1;
    }
}


console.log(rotate([2,5,1,4,8], 2));
