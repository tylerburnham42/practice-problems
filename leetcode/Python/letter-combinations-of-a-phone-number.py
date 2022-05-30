# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        letter_to_num = {
            2: ["a","b","c"],
            3: ["d","e","f"],
            4: ["g","h","i"],
            5: ["j","k","l"],
            6: ["m","n","o"],
            7: ["p","q","r", "s"],
            8: ["t","u","v"],
            9: ["w","x","y", "z"],
        }
        
        out_strs = []
        
        
        for digit in digits:
            #print("Digit", digit)
            if len(out_strs) == 0:
                out_strs.extend(letter_to_num[int(digit)])
                #print("Base Case", out_strs)
            else:
                new_strs = []
                for old_str in out_strs:
                    #print("old str", old_str)
                    for letter in letter_to_num[int(digit)]:
                        #print("letter", letter)
                        new_strs.append(old_str + letter)
                        #print(new_strs)
                        
                out_strs = new_strs
                        
        return out_strs