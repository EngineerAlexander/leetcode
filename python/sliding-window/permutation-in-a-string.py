# Given two strings s1 and s2, return true if s2 contains 
# a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations 
# is the substring of s2.

# Constraints:
# s1 and s2 consist of lowercase English letters.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = {}
        s2_count = {}

        # Count the frequency of each character in s1 and s2 initial window of size s1
        for i in range(len(s1)):
            s1_count[s1[i]] = 1 + s1_count.get(s1[i], 0)
            s2_count[s2[i]] = 1 + s2_count.get(s2[i], 0)

        # Check if the initial window is a permutation of s1
        if s1_count == s2_count:
            return True

        # Slide the window to the right and check if the window is a permutation of s1
        left = 0
        for right in range(len(s1), len(s2)):
            s2_count[s2[right]] = 1 + s2_count.get(s2[right], 0)
            s2_count[s2[left]] -= 1

            if s2_count[s2[left]] == 0:
                del s2_count[s2[left]]

            left += 1

            if s1_count == s2_count:
                return True

        return False