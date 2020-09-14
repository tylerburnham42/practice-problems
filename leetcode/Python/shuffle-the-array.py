# Leetcode 7/31/20
# https://leetcode.com/problems/shuffle-the-array/
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        list1 = nums[:n]
        list2 = nums[n:]
        new_list = []
        
        for index in range(n):
            new_list.append(list1[index])
            new_list.append(list2[index])
            
        return new_list
