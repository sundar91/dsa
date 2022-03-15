function countTriplets(A, B){

    let n = A.length;

    let c = 0
    for(let i = 0; i < n; i++){

        //smaller count
        let smaller = 0;
        for(let j = i -1; j >=0; j--){
            if(A[i] > A[j]) {
                smaller++;
            }

        }

        let larger = 1;
        for(let j =i+1; j < n; j++){
            if(A[i] < A[j]){
                larger++;
            }
        }

        c += (smaller * larger);
    }
    return c;
}

let a  = countTriplets([1, 6, 4, 2, 6, 9]);
console.log(a);
