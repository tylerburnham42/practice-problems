# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/
# Not quite working but close.

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        self.vals = set()
        self.target = target
        self.result = []
        for num in candidates:
            if num <= target:
                self.vals.add(num)
                
        self.sumRecursive(0, [])
        return self.result
        
    
    def sumRecursive(self, num: int, nums: List[int]):
        if num:
            nums.append(num)
        
        total = sum(nums)
        print(nums, total)
        if total == self.target:
            self.result.append([*nums])
            return
        
        if total > self.target:
            return
        

        
        for val in self.vals:
            result = self.sumRecursive(val, nums)
            nums.pop()
            if result:
                out.append(result)