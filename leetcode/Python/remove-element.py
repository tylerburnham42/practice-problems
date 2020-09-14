# Leetcode 7/26
# https://leetcode.com/problems/remove-element/submissions/
# This problem is not meant for python with a del keyword. 

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        index = 0
        while index < len(nums):
            if nums[index] == val:
                del nums[index]
            else:
                index += 1
        return