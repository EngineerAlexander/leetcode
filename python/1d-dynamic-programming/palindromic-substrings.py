# Given a string s, return the number of palindromic substrings in it.

# A string is a palindrome when it reads the same backward as forward.

# A substring is a contiguous sequence of characters within the string.

# Constraints:
# s consists of lowercase English letters.

class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        if length == 0:
            return 0
        elif length == 1:
            return 1

        num_valid = 0
        for i in range(length):
            # All odd numbered valid palindromic substrings centered at i
            l = i
            r = i
            while (l >= 0) and (r < length) and (s[l] == s[r]):
                num_valid += 1
                l -= 1
                r += 1

            # All even numbered valid palindromic substrings centered at i, and i+1
            l = i
            r = i + 1
            while (l >= 0) and (r < length) and (s[l] == s[r]):
                num_valid += 1
                l -= 1
                r += 1

        return num_valid
    
# Time complexity: O(n^2) to check all palindromic substrings
# Space complexity: O(1) only using a few variables