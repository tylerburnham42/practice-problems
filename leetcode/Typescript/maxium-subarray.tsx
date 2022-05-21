// maxium subarray leetcode #53
// Completed 5-20-2022
function maxSubArray(nums: number[]): number {
    
    var sum = 0
    var maxSum = nums[0]
    
    for (var num of nums) {
        sum += num
        if (num > sum) {
            sum = num
        }
        if (maxSum < sum) {
            maxSum = sum
        }
    }
    return maxSum
};