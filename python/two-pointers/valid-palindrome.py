# A phrase is a palindrome if, after converting all uppercase letters into 
# lowercase letters and removing all non-alphanumeric characters, it reads 
# the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.
# Constraints:
# s consists only of printable ASCII characters.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)

        ptr1 = 0
        ptr2 = length - 1

        while ptr1 <= ptr2:
            char1 = s[ptr1]
            char2 = s[ptr2]

            # skip non-letters
            if not char1.isalnum():
                ptr1 += 1
                continue
            if not char2.isalnum():
                ptr2 -= 1
                continue

            # compare lowercase
            if char1.lower() != char2.lower():
                return False

            ptr1 += 1
            ptr2 -= 1

        return True
    
# Time complexity: O(n)
# Space complexity: O(1)