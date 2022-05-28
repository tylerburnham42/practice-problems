# 394. Decode String
# https://leetcode.com/problems/decode-string/
# Solved using recursion.

class Solution:
    def decodeString(self, s: str) -> str:
        #print("S:", s)
        final_str = ""
        if len(s) == 0:
            return ""
        
        got_brace = False
        tmp_str = ""
        tmp_num = ""
        open_counter = 0
        for char in s:
            #print(char, ":", tmp_str, ":", tmp_num, ":", open_counter)
            if got_brace:
                if char == "[":
                    open_counter += 1

                elif char == "]":
                    if not open_counter:
                        final_str += self.decodeString(tmp_str) * int(tmp_num)
                        got_brace = False
                        tmp_str = ""
                        tmp_num = ""
                        continue
                    else:
                        open_counter -= 1

                tmp_str += char
                    
            elif char == "[":
                got_brace = True
                
            elif char.isdigit():
                tmp_num += char
                
            else:
                final_str += char
            
        
        return final_str