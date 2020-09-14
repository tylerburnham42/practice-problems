/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    var sum = 0
    var arr = []
    var i
    for (i in nums) {
        sum += parseInt(nums[i])
        arr.push(sum)
    }
    return arr
};