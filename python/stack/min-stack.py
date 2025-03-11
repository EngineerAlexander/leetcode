# Design a stack that supports push, pop, top, and 
# retrieving the minimum element in constant time.
# Implement the MinStack class:
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.
# Constraints:
# Methods pop, top and getMin operations will always be called on 
# non-empty stacks.

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.min_stack.append(val)
        else:
            minimum = min(val, self.min_stack[-1])
            self.min_stack.append(minimum)

        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Time complexity: O(1) init, O(1) push, O(1) pop, O(1) top, O(1) getMin
# Space complexity: O(n) where n is the number of elements in the stack