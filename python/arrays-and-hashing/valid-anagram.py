# Given two strings s and t, return true if t is an anagram of s, 
# and false otherwise.
# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        letters = {}
        for el in s:
            if el in letters:
                letters[el] += 1
            else:
                letters[el] = 1

        for el in t:
            if el in letters:
                letters[el] -= 1
                if letters[el] == 0:
                    del letters[el]
            else:
                return False
        return True
    
# Time complexity: O(n)
# Space complexity: O(n)