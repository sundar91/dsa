
// dynamic programming
// const towerHopper = (towers)=>{
//     return is_hoppable(0, towers);
// }
// const is_hoppable = (index, towers)=>{
//     if(towers.length <= index) return true;

//     let maxJump = towers[index];
//     if( maxJump === 0) return false;

//     for(let i = 1; i <= maxJump; i++){
//         if( is_hoppable(index + i , towers)){
//             return true;
//         }
//     }
//     return false;
// }


const is_hoppable = (towers) =>{
    let current = 0; 
    while(true){
        if(current >= towers.length)
            return true;

        if(towers[current] === 0) return false;
        
        current = next_step(current, towers);
    }

}

const next_step= (index, towers) =>{

}


console.log(towerHopper([4,2,0,0,2,0]))

console.log(towerHopper([1,0]))

