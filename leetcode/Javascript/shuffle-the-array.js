/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number[]}
 */
var shuffle = function(nums, n) {
    var back = nums.slice(n)
    var front = nums.slice(0,n)
    var new_arr = []
    var min = Math.min(back.length, front.length)
    
    for (var i=0; i<min; i++){
        new_arr.push(front[i])
        new_arr.push(back[i])
    }
    
    return new_arr
};