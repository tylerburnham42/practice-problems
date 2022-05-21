/**
 * Rotate Array Leetcode #189
 * Solved 5-21-2022
 * Solved using cyclic replacement
 * 
 Do not return anything, modify nums in-place instead.
 */
 function rotate(nums: number[], k: number): void {
    var cycleIndexStart = 0
    var curIndex = 0
    var toReplaceIndex = k % nums.length
    var previousNum = nums[curIndex]
    var currentNum = 0
    var numbersReplaced = 0
    
    while (numbersReplaced < nums.length -1) {
        //console.log("CycleIndex", cycleIndexStart)
         do {
            currentNum = nums[toReplaceIndex] 
            nums[toReplaceIndex] = previousNum
            numbersReplaced += 1
            //console.log("Previous Num", previousNum)
            //console.log("Current Num", currentNum)

            previousNum = currentNum
            curIndex = toReplaceIndex
            toReplaceIndex = (curIndex + k) % nums.length
            
            //console.log("Nums Replaced", numbersReplaced)
            //console.log("Nums", nums)

        } while (toReplaceIndex != cycleIndexStart);
        //console.log("End of cycle")
        
        nums[toReplaceIndex] = previousNum
        numbersReplaced += 1
        //console.log("Nums", nums)
        cycleIndexStart += 1
        curIndex = cycleIndexStart
        toReplaceIndex = cycleIndexStart + (k % nums.length)
        previousNum = nums[cycleIndexStart]
    }

};