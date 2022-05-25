# Sign of the Product of an array. #1822
# https://leetcode.com/problems/sign-of-the-product-of-an-array/

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negative = False

        for num in nums:
            if num == 0:
                return 0
            
            if num < 0:
                negative = not negative
                
        if negative:
            return -1
        else:
            return 1