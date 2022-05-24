# Three Sum #15
# Needed to look at a soultion to get it should probably revisit.
# Solved 5-22-2022

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        positive = []
        negative = []
        zeros = []
        output = []
        
        
        # First Remove the Tripled Numbers so there are no duplicates in the output.
        # This is a little redundent with the casting to set.
        new_nums = []
        nums_counter = {}
        for num in nums:
            if num in nums_counter:
                if nums_counter[num] >= 1:
                    nums_counter[num] += 1
                    continue #Skip this triple
                else:
                    nums_counter[num] += 1
            else:
                nums_counter[num] = 1
                
            new_nums.append(num)
        

        # Break the list up into positive and negative halves.
        for num in new_nums:
            if(num > 0):
                positive.append(num)
            elif(num < 0):
                negative.append(num)
            else:
                zeros.append(num)
                
        positive.sort()
        negative.sort()
        #print(negative)
        
        # Cast them into sets for a O(1) lookup time
        positive_set = set(positive)
        negative_set = set(negative)
        
        # We filtered out the triple zero case so check if it is valid
        zeros_count = 0
        if 0 in nums_counter:
            if(nums_counter[0] >= 3):
                output.append([0,0,0])
            del nums_counter[0]
        
        #Check each pair of numbers if the corrisponding sum is not in the dict.
        for num in nums_counter.keys():
            count = nums_counter[num]
            if(count >=2):
                if num * -2 in nums_counter:
                    output.append([num, num, num * -2])
                
        # Check the case where we have at least 1 zero and a corrisponding -num and +num exist
        if(len(zeros) > 0):
            for num in negative_set:
                if (num * -1 in positive_set):
                    output.append([num * -1, 0, num])
                
                
        # Go through each pair of positive numbers and check if the -num exists
        for i in range(len(positive)):
            for j in range(i+1,len(positive)):               
                subtract = (positive[i] + positive[j]) * -1
                if (subtract in negative_set):
                    output.append([positive[i], positive[j], subtract])

                    
        # Go through each pair of negative numbers and check if the +num exists
        for i in range(len(negative)):
            for j in range(i+1,len(negative)):
                add = (negative[i] + negative[j]) * -1
                if (add in positive_set):
                    output.append([negative[i], negative[j], add])

                    
        return output