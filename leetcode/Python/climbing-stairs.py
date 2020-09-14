# Leetcode 7/21
# This is a simple fibonacci problem. This useses recursion and memoization.
# https://leetcode.com/problems/climbing-stairs

class Solution:
    cache = {}
    
    def climbStairs(self, n: int) -> int:
        return self.fib(n+1)
    
    def fib(self, n: int):
        if n <= 1:
            return n
        elif n in self.cache:
            return self.cache[n]
        else:
            value = self.fib(n - 1) + self.fib(n - 2)
            self.cache[n] = value
            return value