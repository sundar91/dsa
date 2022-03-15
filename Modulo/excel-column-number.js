// Given a column title as appears in an Excel sheet, return its corresponding column number.

const titleToNumber = (A)=>{
    let sum = 0;
    let init = "A".charCodeAt() - 1;
    let pw = 1;

    for(let i = A.length - 1; i >=0; i--){
        let charNum = A[i].charCodeAt() % init;
        sum += (charNum * pw)
        pw = pw * 26
    }
    return sum;
}

console.log(titleToNumber('AA')) 