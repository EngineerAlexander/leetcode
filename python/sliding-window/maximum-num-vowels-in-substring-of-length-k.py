# Given a string s and an integer k, return the maximum 
# number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        length = len(s)
        left = 0
        right = k - 1

        vowels = set(['a', 'e', 'i', 'o', 'u'])

        # count initial window
        num_vowels = 0
        for i in range(0, k):
            if s[i] in vowels:
                num_vowels += 1

        # sliding window keeping track of max
        max_vowels = num_vowels
        while (right + 1)< length:
            if s[left] in vowels:
                num_vowels -= 1
            if s[right + 1] in vowels:
                num_vowels += 1
            left += 1
            right += 1
            max_vowels = max(max_vowels, num_vowels)

        return max_vowels

# Time complexity: O(n)
# Space complexity: O(1)