# 1578. Minimum Time to Make Rope Colorful
# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
# Really dumb soultion attempting to use recursion. It does not completely work but it close.

class Solution:
    memo = {}
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        #print("NeededTime", neededTime)
        return self.minCostRecur(colors, neededTime)
        
    def minCostRecur(self, colors, neededTime, smallest = 0, indent = ""):
        print(indent + "Top  Colors:", colors, smallest)
        
        if len(colors) == 1:
            return 0
        
        last = 0
        min_count = 0
        for i in range(1, len(colors)):
            if colors[i] == " ":
                continue
                
            elif colors[i] == colors[last]:
                
                
                left = list(colors)
                left[i] = " "
                left_str = "".join(left)
                if (left_str not in self.memo):
                    self.memo[left_str] = self.minCostRecur(left_str, neededTime, smallest, indent + "  ") + neededTime[i]
                
                right = list(colors)
                right[last] = " "
                right_str = "".join(right)
                if (right_str not in self.memo):
                    self.memo[right_str] = self.minCostRecur(right_str, neededTime, smallest, indent + "  ") + neededTime[last]
                    
                smallest += min(self.memo[left_str], self.memo[right_str])
                print(indent + "i=", i, "last=", last, (left_str, self.memo[left_str]), (right_str, self.memo[right_str]), smallest)
                return smallest
                
            #print("Smallest", smallest)
            
            last = i
        print(indent + "End:", colors, self.memo, smallest)
        return smallest


# Actually working version
from queue import PriorityQueue

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        duplicates = []
        time = 0
        for index in range(0, len(colors)):
            #print(colors[index], duplicates)
            if len(duplicates) == 0 :
                duplicates.append(index)
            
            elif(colors[index] == colors[duplicates[-1]]):
                duplicates.append(index)
                
            else:
                if len(duplicates) >= 2:
                    times = PriorityQueue()
                    for num in duplicates:
                        times.put(neededTime[num])
                    
                    while(times.qsize() >= 2):
                        time += times.get()
                        #print(time)
                duplicates = [index]
        
            #print(colors[index], duplicates, time)
        if len(duplicates) >= 2:
            times = PriorityQueue()
            for num in duplicates:
                times.put(neededTime[num])

            while(times.qsize() >= 2):
                time += times.get()
                #print(time)
        return time