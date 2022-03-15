function diagonal(A){
        let m = A.length;

        let td = m + m -1
     
        let C = Array(m).fill(0).map(() => Array(td).fill(0));
        let i = 0
        let k = 0
        for(let j = 0; j< m; j++){
            let I = i 
            let J = j 
            let z = 0
            while(I < m && J >=0){
                C[k][z] = A[i][j]
                I += 1
                J -= 1
                z += 1
            }
            k += 1
        }
        
        j = m - 1
        for(let i=0; i< m; i++){
           let  I = i
           let J = j
            z = 0
            
            while(I < m && J >= 0){
                C[k][z] = A[i][j];
                I += 1
                J -= 1
                z += 1
            }
            k +=1

        return C;
        }
}

