"""Design a stack class that supports the push, pop, top, and getMin operations.

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack
    Each function should run in O(1) time."""


class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min) == 0:
            self.min.append(val)
        else:
            self.min.append(min(val, self.min[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.min) > 0:
            return self.min[-1]
        else:
            return None


minStack = MinStack()
print(minStack.push(1))
print(minStack.push(2))
print(minStack.push(0))
# print(minStack.push(4))
print(minStack.getMin())
print(minStack.pop())
print(minStack.top())
print(minStack.getMin())
