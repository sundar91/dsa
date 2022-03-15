const maxSubArray = (nums) =>{
    if(!nums || nums.length < 1) return null;

    if(nums.length == 1)
        return nums[0];

    let maxSum = nums[0], 
    sum = nums[0];
    for(let i = 1; i < nums.length ; i++){
        
        sum = Math.max(nums[i], sum + nums[i]);

        if(sum > maxSum){
             maxSum = sum;
        }
    }

    return  maxSum;
}

console.log(maxSubArray([1]));
console.log(maxSubArray([1]));
console.log(maxSubArray([1,5,6,-7,8]));

console.log(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]));
console.log(maxSubArray([5,4,-1,7,8]));
console.log(maxSubArray([-2,1]));
console.log(maxSubArray([-1,0,-2]))