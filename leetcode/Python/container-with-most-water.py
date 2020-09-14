# This is a naiive approach that is O(n^2)
# Leetcode 7/17
# I need to go back and do this one again. 
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        index2 = 0
        arr_length = len(height) - 1
        # The minus one is we have to check in pairs so we can skip the last since its covered by the before.
        for index in range(arr_length):
            index2 = arr_length
            
            if (arr_length - index) * height[index] < max_area:
                continue
            
            while index2 != index:
                length = index2 - index
                width = min(height[index], height[index2])
                area = length * width
                # print(index, index2, length, width, area)
                if area > max_area:
                    max_area = area
                
                print(index, index2)
                index2 -= 1
        return max_area