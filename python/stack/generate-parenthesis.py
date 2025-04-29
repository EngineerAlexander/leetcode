# Given n pairs of parentheses, write a function to generate 
# all combinations of well-formed parentheses.

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        If openN == closedN we have found result
        if openN < N we add open
        if openN > closedN we add closed
        """
        stack = []
        res = []
        def backtracking(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
            if openN < n:
                stack.append("(")
                backtracking(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtracking(openN, closedN + 1)
                stack.pop()

        backtracking(0, 0)
        return res
    
