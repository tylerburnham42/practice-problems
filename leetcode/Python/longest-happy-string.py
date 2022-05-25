# Longest Happy String #1405
# https://leetcode.com/problems/longest-happy-string/
# This soultion is kinda jank I should re do this.

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        abc_dict = [['a', a], ['b', b], ['c', c]]
        last_char = ""
        last_count = 0
        longest_string = ""
        
        while(len(abc_dict)>=1):
            
            
            abc_dict.sort(key = lambda x:x[1], reverse=True)
            #print(f"Dict: {abc_dict}")
                             
            for i in range(len(abc_dict)):
                letter, count = abc_dict[i]
                #print(f"letter = {letter}, count = {count}")
                #print(f"prev_letter = {last_char}, prev_count = {last_count}")
                
                if letter == last_char:
                    continue
                
                if count == 0:
                    del abc_dict[i]
                    break
                
                if count >= 2:
                    if last_count > count:
                        longest_string += letter
                        abc_dict[i][1] -= 1
                        
                    else:
                        longest_string += letter * 2
                        abc_dict[i][1] -= 2
                        
                elif count == 1:
                    longest_string += letter
                    abc_dict[i][1] -= 1
                    

                
                last_char = letter
                last_count = abc_dict[i][1]
                    
                #print(f"longest_string {longest_string}\n")
                break
                    
            if(len(abc_dict)==1 and abc_dict[0][0]==last_char):
                break
        return longest_string