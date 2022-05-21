// Typescript binary search
// Written 5-20-2022
function search(nums: number[], target: number): number {
    var start = 0
    var end = nums.length - 1
    var middle = undefined

    while (start <= end) {
        middle = Math.ceil((end+start-1)/2)
        //console.log(start, middle, end)
        if (nums[middle] == target) {
            return middle
        }
        if (start == end) {
            return -1
        }
        else if (nums[middle] < target) {
            start = middle +1
        }
        else {
            end = middle
        }
        
    }
    
    return -1
};