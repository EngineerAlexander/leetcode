# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. 
# The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated 
# by a single space.

# Note that s may contain leading or trailing spaces or multiple 
# spaces between two words. The returned string should only have 
# a single space separating the words. Do not include any extra spaces.

class Solution:
    def reverseWords(self, s: str) -> str:
        split_s = s.split()
        return " ".join(split_s[::-1])
    
# Time complexity: O(n) to split the string and join it back
# Space complexity: O(n) for the split string