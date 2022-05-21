/**
 * Merge Sorted Arrays
 * Completed 5-20-2022
 * This is kinda jank but it does work
 * 
 Do not return anything, modify nums1 in-place instead.
 */
 function merge(nums1: number[], m: number, nums2: number[], n: number): void {
    var mergedArr = []
    var index1 = 0
    var index2 = 0
    
    while ( index1 <= m-1 || index2 <= nums2.length -1 ) {
        //console.log(mergedArr, index1, index2)
        if (index1 > m-1) {
            mergedArr.push(nums2[index2])
            index2 ++
        }
        else if (index2 > nums2.length -1) {
            mergedArr.push(nums1[index1])
            index1 ++
        }
        else if(nums1[index1] <= nums2[index2]) {
            mergedArr.push(nums1[index1])
            index1 ++
        }
        else {
            mergedArr.push(nums2[index2])
            index2 ++
        }
    }
    //console.log("Done,", mergedArr)
    //nums1 = mergedArr.slice(0)
    nums1.splice(0, nums1.length, ...mergedArr);
};