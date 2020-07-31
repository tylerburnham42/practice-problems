# Leetcode 7/30
# Running Sum of 1d Array
# One line answer with list comprehension
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return [sum(nums[:x+1]) for x in range(len(nums))]