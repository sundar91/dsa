const reverse = (num)=>{
    var revnum = 0;
    for( var i = 0; i < 32; i++ ) {
      if( num&1<<i)
        revnum |= 1<<(31-i);
    }
    return revnum>>>0;
}

console.log(reverse(3))