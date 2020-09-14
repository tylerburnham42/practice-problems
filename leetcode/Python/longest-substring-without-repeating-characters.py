# Longest Substring without repeating characters - 7/6/2020
# https://leetcode.com/problems/longest-substring-without-repeating-characters

import queue
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        found = {}
        order = queue.SimpleQueue()
        count = 0
        largest = 0
        for letter in list(s):
            if letter in found:
                if count > largest:  
                    largest = count
                    
                while True:
                    oldest = order.get()
                    count -= 1
                    del found[oldest]
                    
                    print(oldest)
                    if order.empty() or oldest == letter:
                        break
                
            
            found[letter] = True
            order.put(letter)
            count += 1

            
        if count > largest:
            largest = count
        return largest