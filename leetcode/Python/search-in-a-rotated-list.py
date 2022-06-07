# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        first = 0
        last = len(nums) - 1
        
        #print(nums)
        while True:
            middle = floor((first+last)/2)
            #print(target, [first, middle, last], [nums[first], nums[middle], nums[last]])
            
            if target == nums[middle]:
                return middle
            
            elif target == nums[first]:
                return first
            
            elif target == nums[last]:
                return last
            
            elif first == last or middle == first:
                break
            
            #The two good cases
            
            #Is right sorted?
            right_sorted =  nums[last] > nums[middle]
            left_sorted =  nums[first] < nums[middle]
            
            if right_sorted and left_sorted:
                #print("Binary search")
                if target > nums[middle]:
                    first = middle + 1
                else:
                    last = middle - 1
                
            elif right_sorted:
                #print("Right")
                if target > nums[last] or target < nums[middle]:
                    #print("Move Left")
                    last = middle - 1
                else:
                    #print("Move Right")
                    first = middle + 1


            elif left_sorted:
                #print("Left")
                if target < nums[first] or target > nums[middle]:
                    #print("Move Right")
                    first = middle + 1
                else:
                    #print("Move Left")
                    last = middle - 1

        return -1