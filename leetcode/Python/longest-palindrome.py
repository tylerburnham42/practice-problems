# 409. Longest Palindrome
# https://leetcode.com/problems/longest-palindrome/
# Copied from codsignal practice. Overkill because the other problem wanted what the longest one actually was.


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = {}
        for letter in s:
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1

        counts_list = list(counts.items())
        #print(counts_list)
        counts_list.sort(key=lambda x: x[0])
        print(counts_list)

        left = ""
        right = ""
        final_char = ""
        for letter, num in counts_list:
            #print(left, right)

            while num >= 2:
                left += letter
                right = letter + right
                num -= 2

            if num == 1 and final_char == "":
                final_char = letter
            elif num == 1:
                continue


        return len(left + final_char + right)