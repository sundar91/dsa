
const maxConsecutive = (A) =>{

    total = 0;
    for(let i of A){
        if(i == 1) total++;
    }

    let l = 0;
    let r = 0;

    let count = 0;
    for(let i= 0; i < A.length; i++){
        if(A[i] == 0){
            l = r;
            r = 0;
        }
        else {
            r++;
        }

        let ans = l + r;

        if( l + r < total ){
            ans = ans + 1;
        }

        count = Math.max(count, ans);
       
       
    }

    return count;

}

console.log(maxConsecutive("111000"))
console.log(maxConsecutive("111011101"))