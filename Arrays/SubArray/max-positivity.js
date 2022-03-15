const maxPositivity = (A)=>{
    
    let maxCount = 0;
    let stPoint = 0;

    let i  = 0;
    let n = A.length;
    while(i < A.length){
        if(A[i] >= 0){
            let continueStPoint = i;
            let continueCount = 0;
            while(A[i] >=0 && i < n){
                i++;
                continueCount++;
            }

            if(continueCount > maxCount){
                maxCount = continueCount;
                stPoint = continueStPoint
            }
        }
        i++;
    }
   
    let maxNums = [];
    for(let i = stPoint; i < stPoint +maxCount; i++){
        maxNums.push(A[i]);
    }

    return maxNums;
}


console.log(maxPositivity([5, -1, 7, 8]))

console.log(maxPositivity([1, 2, 3, 4, 5, 6]))

