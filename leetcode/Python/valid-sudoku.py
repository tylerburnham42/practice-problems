import collections


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        # Check Lines
        for line in board:
            if not self.listToValid(line):
                return False
            
        for line in list(zip(*board)):
            if not self.listToValid(line):
                return False
        
        quadrants = collections.defaultdict(list)
        y = 0
        for line in board:
            quadrants[str(int(y/3)) + str(0)].extend(line[:3])
            quadrants[str(int(y/3)) + str(1)].extend(line[3:6])
            quadrants[str(int(y/3)) + str(2)].extend(line[6:])
            y += 1
                
        for line in quadrants.values():
            if not self.listToValid(line):
                return False
        
            
        return True
        
    def listToValid(self, nums):
        nums = sorted(list("".join(nums).replace(".", "")))
        #print(nums)
        for n in range(1, len(nums)):
            if nums[n] == nums[n-1]:
                return False
        
        return True