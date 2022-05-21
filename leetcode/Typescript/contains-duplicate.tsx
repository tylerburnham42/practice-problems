// Contains Duplicate #217 on leetcode
// Solved 5-20-2022
function containsDuplicate(nums: number[]): boolean {
    let setNums = new Set<number>(nums);
    return (setNums.size != nums.length)
};