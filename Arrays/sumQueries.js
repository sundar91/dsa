const sumQueries = (arr, q)=>{
    let n = arr.length;
    let sum =[arr[0]];
    for(let i = 1; i < n; i++){
        sum = sum[i-1] + arr[i];
    }

    for(let i = 0; i < q.length; i++){
        let s = q[0];
        let e = q[0];
        if(i === 0){
            console.log(sum[e]);
        }
        else{
            console.log(sum[e] - sum[s-1]);
        }
    }
}

sumQueries([-3, ], []);
