const permutation = (s,t)=> {
    let charset = {};
    for(let str of s){
        if(str in charset) charset[str]++;
        else charset[str] = 1;
    }

    for(let str of t){
        if(str in charset){
            charset[str]--;
            if(charset[str] < 0) return false;
        }
        else {
            return false;
        }
    }
    return true;
}

console.log(permutation('dog','god'))
console.log(permutation('odg','god'))
console.log(permutation('asdasd','god'))


const permutationBySorting = (s,t)=>{
    let sortS = s.split('').sort().join('');
    let sortT = t.split('').sort().join('');
    return sortS === sortT;    
}


console.log(permutationBySorting('dog','god'))
console.log(permutationBySorting('odg','god'))
console.log(permutationBySorting('asdasd','god'))