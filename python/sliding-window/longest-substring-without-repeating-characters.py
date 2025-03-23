#Given a string s, find the length of the longest 
# substring without duplicate characters.

# Constraints:
# s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        start = 0
        seen = set()
        longest = 0

        for end in range(length):
            if s[end] not in seen:
                seen.add(s[end])
                longest = max(longest, end - start + 1)
            else:
                while s[start] != s[end]:
                    seen.remove(s[start])
                    start += 1
                start += 1

        return longest
    
# Time complexity: O(n)
# Space complexity: O(1), because constraints say that there are only 128 ASCII characters so that is our upper bound.