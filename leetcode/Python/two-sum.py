# Two Sum - 7/5/2020
# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = 0
        nums = [[x, nums[x]] for x in range(len(nums))]
        nums = sorted(nums, key=itemgetter(1))
        
        
        index_1 = 0
        index_2 = 1
        
        while index_1 + 1 < len(nums):
            
            if(index_2 + 1 > len(nums) or nums[index_1][1] + nums[index_2][1] > target):
                index_1 += 1
                index_2 = index_1

            elif(nums[index_1][1] + nums[index_2][1] == target):
                return [nums[index_1][0], nums[index_2][0]]
            
            index_2 += 1
            