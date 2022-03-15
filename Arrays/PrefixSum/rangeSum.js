const rangeSum = (A, B) => {
    let n = A.length;
    var pf = [];
    pf[0] = A[0];
    // calculate prefix sum (cumulative sum)
    for(let i = 1; i < n; i++){
        pf[i] = pf[i-1] + A[i];
    }
    var sums = [];
    for(let i = 0 ; i < B.length; i++){
       var s = B[i][0];
       var e = B[i][1];
       var sum= 0;
       if(s == 1){
        sum = pf[e-1];
       }
       else{
        sum = pf[e-1] - pf[s-1-1];
       }
       sums.push(sum);
    }
    return sums;
}