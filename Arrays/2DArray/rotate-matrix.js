function rotateMatrix(A){ 
    let m = A.length;
    let n = A[0].length;

    for(let i = 0; i < m; i++){
        for(let j = i+1; j < n; j++){
            let temp = A[i][j];
            A[i][j] = A[j][i];
            A[j][i] = temp;
         }
    }

    for(let i = 0; i < m; i++){
        let k = 0;
        let j = m-1;
        while(k<j){
            let temp = A[i][k];
            A[i][k] = A[i][j];
            A[i][j] = temp;
            k++;
            j--;
        }
    }  

    return A;
} 