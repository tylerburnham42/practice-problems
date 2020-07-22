# Leetcode 7/22
# https://leetcode.com/problems/count-and-say/
class Solution:
    def countAndSay(self, n: int) -> str:
        
        num = "1"
        new_num = ""
        for x in range(n - 1):
            
            last = num[0]
            count = 0
            
            # Loop through the count and say num string
            for val in num:
                # print("val=", val)
                # print(count, last, val)
                
                # Check if its the end of a repetition
                if last != val:
                    # print(count, last)
                    # add it to the string
                    new_num += str(count)
                    new_num += str(last)
                    count = 1
                else:
                    count += 1

                last = val
            
            if last != "":
                # print(count, last)
                new_num += str(count)
                new_num += str(last)
            
            # print("num=", new_num)
            num = new_num
            new_num = ""
            
        return num
