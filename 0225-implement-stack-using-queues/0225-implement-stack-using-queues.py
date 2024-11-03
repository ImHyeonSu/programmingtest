class MyStack:
    def __init__(self):
        self.my_stack = []

    def push(self, x: int) -> None:
        self.my_stack.append(x)

    def pop(self) -> int:
        last_value = self.my_stack[-1]
        del self.my_stack[-1]
        return last_value

    def top(self) -> int:
        return self.my_stack[-1]

    def empty(self) -> bool:
        return len(self.my_stack) == 0

        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()