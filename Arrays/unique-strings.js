const isUniqueChars = (string)=>{

    let charset = {};
    for(let str of string){
        if(str in charset) return false;
        charset[str] = true;
    }
    return true;
}

console.log(isUniqueChars('hell'));
console.log(isUniqueChars('abcdefghijklmno'));


//using bit vetor
const isUnique = (string)=>{
    let checker = 0;
    for(let index in string){
        const val =  string.charCodeAt(index) - 'a'.charCodeAt(0);
        if((checker & (1 << val)) > 0) return false;

        checker = checker | 1 << val;
    }

    return true;
}

console.log(isUnique('hell'));
console.log(isUnique('abcdefghijklmno'));


