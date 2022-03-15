 // O(n^2)
var twoSum = function(nums, target) {
    for(let i = 0; i < nums.length; i++){
        for(let j = i +1; j < nums.length; j++){
            if(nums[i] + nums[j] === target) return true;
        }
    }
     return false;
 };
 



var twoSum1 = (nums, target)=>{
    let cache = {};
    for(let i = 0; i < nums.length; i++){
        let remaining = target - nums[i];
        if(remaining in cache){
            return [ cache[remaining], nums[i]]
        }
        cache[nums[i]] = i;
    }
    return null;
}


const pairSum = (arr, target) =>{
    let data = {};
    for(let a of arr){
        let rem = target - a;
        if(rem in data){
            return true;
        }
        data[a] = true;
    }
    return false;
}

console.log(pairSum([8,9,5, -2], 6))