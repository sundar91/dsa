// left shift
// const checkBit = (N, i) => {

//     if( N & (1 << i)) return true;
//     return false;

// }


// right shift
const checkBit = (N, i) => {

    if( 1 & (N >> i)) return true;
    return false;

}

console.log(checkBit(29, 2))