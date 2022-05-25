# Reverse Words in a String #151
# One line python soultion. 
# https://leetcode.com/problems/reverse-words-in-a-string/
# Solved 5-21-2022
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.strip().split()[::-1])
