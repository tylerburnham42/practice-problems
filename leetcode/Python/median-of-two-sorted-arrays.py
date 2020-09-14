# Leetcode Nedian of Two Sorted Arrays 7/7/2020
# This is the naive soultion. I need to go back and do the binary search at some point.  
# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_nums = sorted(nums1 + nums2)
        
        length = len(new_nums)
        if length % 2 == 0:

            lower_half = int(length / 2) - 1
            upper_half = int(length / 2)
            return (new_nums[lower_half] + new_nums[upper_half])/2

        else:
            return new_nums[int(length / 2)]
        