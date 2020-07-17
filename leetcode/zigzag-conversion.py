# Leetcode 7/17
# https://leetcode.com/problems/zigzag-conversion
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        
        index = 0
        going_up = True
        letters = {}
        for letter in s:
            if index in letters:
                letters[index] += letter
            else:
                letters[index] = letter
            
            # Change Direction
            if index == numRows - 1:
                going_up = False
            elif index == 0:
                going_up = True
            
            # Move up or down
            if going_up:
                index += 1
            else:
                index -= 1
        
        out = ""
        for index in range(numRows):
            if index in letters:
                out += letters[index]
            
        return out