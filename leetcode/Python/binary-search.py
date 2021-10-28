# Recursive soultion binary search.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.recursive_search(nums, target, 0)
        
        
    def recursive_search(self, nums: List[int], target: int, start_index: int) -> int:
        if len(nums) == 0:
            return -1
        
        middle = (len(nums) - 1) // 2
        
        #print(len(nums), middle, nums, target, start_index)
        if nums[middle] == target:
            return start_index+middle

        elif nums[middle] > target:
            return self.recursive_search(nums[:middle], target, start_index)
            
        else:
            return self.recursive_search(nums[middle+1:], target, start_index+middle+1)