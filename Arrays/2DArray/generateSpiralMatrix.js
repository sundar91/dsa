const generateMatrix = (A)=>{
    let C = Array(A).fill(0).map(()=> Array(A).fill(0));
     count = 1;
     let i = 0;
     let j = 0;
     while(A > 0){


         for(let k = 0; k < A - 1; k++){
             C[i][j] = count++;
             j++;
         }

         for(let k= 0; k < A-1; k++){
             C[i][j] = count++;
             i++;
         }

         for(let k= 0; k < A-1; k++){
             C[i][j] = count++;
             j--;
         }

         for(let k= 0; k < A-1; k++){
             C[i][j] = count++;
             i--;
         }
         
         A = A -2;
         i++;
         j++;
     }

     if(A == 1){
         C[i][j]= count;
     }
     return C;
 }

