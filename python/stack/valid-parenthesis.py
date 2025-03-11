# Given a string s containing just the characters 
# '(', ')', '{', '}', '[' and ']', determine if the 
# input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Constraints:
# s consists of parentheses only '()[]{}'

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '[', }
        
        if (len(stack)%2) != 0:
            return False 

        for char in s:
            if char not in mapping.keys():
                stack.append(char)
            else:
                matching = mapping[char]
                if (len(stack) > 0) and (stack[-1] == matching):
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True

        return False

# Time complexity: O(n)
# Space complexity: O(n)