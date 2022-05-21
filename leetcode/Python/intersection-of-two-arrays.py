# Intersection of two arrays # 350
# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Solved 5-21-2022
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        counter = {}
        output_arr = []
        
        for num in nums1:
            
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
                
        for num in nums2:
            if num in counter:
                output_arr.append(num)
                if counter[num] <= 1:
                    del counter[num]
                else:
                    counter[num] -= 1
        
        return output_arr