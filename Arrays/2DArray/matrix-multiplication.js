const solve = (A, B)=>{

    let m = A.length
    let p = B[0].length
    let n = A[0].length
    C = Array(m).fill(0).map(()=> Array(p).fill(0));

    for(let i = 0; i < m; i++){
        for(let j = 0; j < p; j++){
            let s = 0;
             for(let k = 0; k < n; k++){
                 s += (A[i][k] * B[k][j])
             }
             C[i][j] = s;
        }
    }

    return C;
}
