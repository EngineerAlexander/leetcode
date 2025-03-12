# You are given an array of strings tokens that represents an arithmetic 
# expression in a Reverse Polish Notation.
# Evaluate the expression. Return an integer that represents the value 
# of the expression. Note that:
# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
# Constraints:
# tokens[i] is either an operator: "+", "-", "*", or "/", 
# or an integer in the range [-200, 200]

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator_map = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b),
        }

        num_stack = []
        for val in tokens:
            if val in operator_map.keys():
                operator = operator_map[val]
                valb = num_stack.pop()
                vala = num_stack.pop()
                res = operator(vala, valb)
                num_stack.append(res)
            else:
                num_stack.append(int(val))

        return num_stack[0]
    
# Time complexity: O(n)
# Space complexity: O(n)