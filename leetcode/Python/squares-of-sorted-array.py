# Squares of Sorted Array #977
# https://leetcode.com/problems/squares-of-a-sorted-array/
# Solved 5-21-2022
# One line soultion.
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([num ** 2 for num in nums])
        