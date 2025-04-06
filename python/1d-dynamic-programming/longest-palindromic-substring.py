# Given a string s, return the longest palindromic substring in s.

# Constraints:
# s consist of only digits and English letters.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        res = ''
        lenRes = 0
        for i in range(length):
            l = i
            r = i
            # check odd starting at middle
            while (l >= 0) and (r < length) and (s[l] == s[r]):
                if (r - l + 1) > lenRes:
                    res = s[l:r + 1]
                    lenRes = r - l + 1
                l -= 1
                r += 1

            # check even starting at middle and one to right
            l = i
            r = i + 1
            while (l >= 0) and (r < length) and (s[l] == s[r]):
                if (r - l + 1) > lenRes:
                    res = s[l:r + 1]
                    lenRes = r - l + 1
                l -= 1
                r += 1

        return res