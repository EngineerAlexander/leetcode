# Two strings are considered close if you can 
# attain one from the other using the following operations:

# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb
# Operation 2: Transform every occurrence of one existing 
# character into another existing character, and do the 
# same with the other character.
# For example, aacabb -> bbcbaa (all a's turn into b's, 
# and all b's turn into a's)
# You can use the operations on either string as many times 
# as necessary.

# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # check if sorted freq array is identical and see if we have the same characters in each
        def classify(word):
            freq = [0]*26
            chars = [False]*26

            for char in word:
                i = ord(char) - ord('a')
                freq[i] += 1
                chars[i] = True

            return (freq, chars)

        freq1, chars1 = classify(word1)
        freq2, chars2 = classify(word2)

        if chars1 != chars2:
            return False

        return sorted(freq1) == sorted(freq2)
    
# Time complexity: O(n)
# Space complexity: O(1), since we are using a fixed size array of 26