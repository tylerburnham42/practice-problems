# 1647. Minimum Deletions to Make Character Frequencies Unique
# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
# Solved witha dictionary as a counter then a heap to do a greedy count.

from queue import PriorityQueue

class Solution:
    def minDeletions(self, s: str) -> int:
        
        counts = {}
        num_to_delete = 0
        
        for letter in s:
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1
                
        #print(counts)
        queue = PriorityQueue()
        for key, val in counts.items():
            queue.put((-val, key))
        
        prev = None
        while not queue.empty():
            count, letter = queue.get()
            
            #print(count, letter, prev, num_to_delete)
            if count == prev:
                if count + 1 != 0:
                    queue.put((count+1, letter))
                num_to_delete += 1

            prev = count
        return num_to_delete