function minCostChristmasTree(A, B){

    let n = A.length;
    let minCost = Infinity;
    for(let i = 0; i < n; i++){

        //smaller count
        let minB = Infinity;
        for(let j = i -1; j >=0; j--){
            if(A[i] > A[j]) {
                minB =  Math.min(B[j], minB);
            }

        }

        let minB2 = Infinity;
        for(let j =i+1; j < n; j++){
            if(A[i] < A[j]){
                minB2 = Math.min(B[j], minB2)
            }
        }

        if(minB == Infinity || minB2 == Infinity) continue;
        let cost = minB + B[i] + minB2;

        minCost = Math.min(minCost, cost);
    }

    return minCost == Infinity ? -1 : minCost;
}

let a  = minCostChristmasTree([1, 6, 4, 2, 6, 9], [2, 5, 7, 3, 2, 7]);
console.log(a);


// find min cost for triplets