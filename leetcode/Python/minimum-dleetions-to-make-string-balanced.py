# 1653. Minimum Deletions to Make String Balanced
# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/
# Solved 5-25-2022

class Solution:
    def minimumDeletions(self, s: str) -> int:
        
        remove_count = 0
        stack = [""]
        
        for letter in s:
            top = stack[-1]
            if top == 'b' and letter == 'a':
                stack.pop()
                remove_count += 1
            else:
                stack.append(letter)
                            
        return remove_count
