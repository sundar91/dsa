
 console.log(rowColZero([
    [18, 50, 0, 22],
    [14,  11,  95, 33],
    [11,  6, 43, 73],
    [22,  23, 73, 25]
  ])
);

// make all rows and col where 0 is present then replace by -1 

function rowColZero(A){
    let m = A.length;
    let n = A[0].length;


    let s = new Set();
    for(let i = 0; i < m ; i++){
        for(let j = 0; j < n; j++){
            if(A[i][j] == 0){
              s.add( i + '_' +j);
            } 
        }
    }

 
    for(let i of s.values()) { 
        let val = i.split('_');
        let row = +val[0];
        let col = +val[1];
        for(let j  = 0; j < n; j++){
            A[row][j] = 0;
        }

        for(let j  = 0; j < m; j++){
            A[j][col] = 0;
        }
    }
    return A;
}