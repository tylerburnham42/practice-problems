# 204. Count Primes
# https://leetcode.com/problems/count-primes/
# Solved using sieve of eratosthenes

class Solution:
    def countPrimes(self, n: int) -> int:
        
        sive = [True] * n
        
        for i in range(2, len(sive)):
            if sive[i]:
                for j in range(i+i,len(sive),i):
                    #print(i, j)
                    sive[j] = False
        
        count = 0
        
        #print(sive[2:])
        return sum([bol for bol in sive[2:]])