const mergeSortedArrays = (array1, array2)=>{

    let result = [];

    for(let i = 0, j= 0; i < array1.length || j < array2.length ;){
        if(array1[i] <= array2[j]){
            result.push(array1[i]);
            i++;
        }
        else{
            result.push(array2[j]);
            j++;
        }
    }
    return result;
}

console.log(mergeSortedArrays([0,3,4,8],[1,2,5,7,9]));