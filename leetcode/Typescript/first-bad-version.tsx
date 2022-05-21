/**
 * Binary Search Soultion
 * Written 5-20-2022
 *
 * The knows API is defined in the parent class Relation.
 * isBadVersion(version: number): boolean {
 *     ...
 * };
 */

 var solution = function(isBadVersion: any) {

    return function(n: number): number {
        
        var start = 0
        var end = n
        var middle: number
        var firstBad = n + 1
        
        while (start<=end) {
            //console.log(start, middle, end)
            middle = Math.floor((start+end)/2)
            
            if(isBadVersion(middle)) {
                if (middle < firstBad) {
                    firstBad = middle
                }
                end = middle - 1
            }
            else {
                start = middle + 1
            }
        }
        return firstBad
    };
};