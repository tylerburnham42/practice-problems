# 1099. Two Sum Less Than K
# https://leetcode.com/problems/two-sum-less-than-k/

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        
        if len(nums) <= 1:
            return -1
        
        nums.sort()
        #print(nums)
        left = 0
        right = 1
        
        close = -1
        while left <= len(nums)-1 and nums[left] <= k:
            right = left + 1
            current_sum = 0
            while right <= len(nums)-1 and current_sum < k:
                #print(left, right)
                current_sum = nums[left] + nums[right]
                if current_sum < k and current_sum > close:
                    #print(nums[left], nums[right], current_sum)
                    close = current_sum
                    
                right += 1
                
            left+=1
            
        return close