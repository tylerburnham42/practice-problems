# Leetcode 7/18
# This is a vertical scan approach. All the dumb edgecases made this code pretty gross.
# https://leetcode.com/problems/longest-common-prefix/submissions/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        if len(set(strs)) == 1:
            return strs[0]
        
        index = 0
        escape = False
        while True:
            char = None
            for word in strs:
                if word ==  "":
                    return ""
                
                if index + 1 > len(word):
                    if index == 0:
                        return word[0]
                    else:
                        return(word[:index])
                

                if char == None:
                    char = word[index]
                elif word[index] != char:
                    if index == 0:
                        return("")
                    else:
                        return(word[:index])
                        

            index += 1
                    
        return ""