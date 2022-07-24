# 1404. Number of Steps to Reduce a Number in Binary Representation to One
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/submissions/
# Solved 7 / 24 / 2022
class Solution:
    def numSteps(self, s: str) -> int:
        
        s = int(s, 2)
        
        count = 0
        while s > 1:
            #print(s, count)
            if s % 2 == 1:
                s += 1
                count += 1
            else:
                s = s // 2
                count += 1
            
        return count