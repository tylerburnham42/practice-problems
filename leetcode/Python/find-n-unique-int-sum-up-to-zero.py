# 1304. Find N Unique Integers Sum up to Zero
# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
# Solved 5-25-2022

class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr = []
        
        if n % 2 == 1:
            arr.append(0)
        
        for i in range(1, floor(n/2)+1):
            arr.append(i)
            arr.append(-i)
            
        return arr
