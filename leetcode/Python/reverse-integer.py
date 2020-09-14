# Leetcode Reverse Integer - 7/6/2020
# https://leetcode.com/problems/reverse-integer

class Solution:
    def reverse(self, x: int) -> int:
        is_negative = -1 if x < 0 else 1
        value = int(''.join(list(str(abs(x))[::-1]))) * is_negative
        
        if value > 2147483647 or value < -2147483647:
            return 0
        
        return value