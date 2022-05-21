// Search Insert Postion # 35 on leetcode
// Solved 5-20-2022
function searchInsert(nums: number[], target: number): number {
    
    var start = 0
    var end = nums.length - 1
    var middle: number
    
    while (start <= end) {
        middle = Math.floor((start+end)/2)
        //console.log(start,middle,end)
        
        if (nums[middle] == target) {
            return middle
        }
        else if (nums[middle] < target) {
            start = middle + 1
            if (start > end) {
                return start
            }
        }
        else {
            end = middle - 1
        }
    }
    return middle
};