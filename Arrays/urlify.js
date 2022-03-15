
// example:
// input: "Mr Josh Smith    ", 13
// output : "Mr%20Josh%20Smith"
// replacing space with %20

const urlify = (str, trueLength)=>{
 
    let charArray = str.split('');

    let spaceCount = 0;
    for(let i = 0; i< trueLength; i++){
        if(str[i] === ' ') spaceCount++;
    }

    let index = trueLength + spaceCount*2 
    // why multiplied by 2? because space will be replaced by %20 so 2 extra indexes required.

    for(let i = trueLength-1; i >= 0; i--){
        if(charArray[i] === ' ' ){
            charArray[index-3] = "%";
            charArray[index-2] = "2";
            charArray[index-1] = "0";
            index = index-3;
        }
        else {
            charArray[index-1] = charArray[i];
            index--;
        }
    }
    return charArray.join('');
}

console.log(urlify("Mr John Smith    ", 13));

