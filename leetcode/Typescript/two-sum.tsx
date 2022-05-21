// Two Sum Leetcode #1
// Solved 5-20-2022
function twoSum(nums: number[], target: number): number[] {
    var searchArr = {}
    
    for (let i = 0; i < nums.length; i++) {
        let current = nums[i]
        //console.log(current, searchArr)
        if (current in searchArr) {
            return [searchArr[current],i]
        }
        else {
            searchArr[target - current] = i
        }
    }
};