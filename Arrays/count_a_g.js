const countAG = (str) =>{
    let count = 0, ans = 0;
    for(let s of str){
        if(s == 'a'){
            count++;
        }
        else if (s == 'g'){
            ans +=count;
        }
    }
    return ans;
}

console.log( countAG('acbagkagg'));