class MyQueue:
    def __init__(self):
        self.my_stack = []

    def push(self, x: int) -> None:
        self.my_stack.append(x)

    def pop(self) -> int:
        last_value = self.my_stack[0]
        del self.my_stack[0]
        return last_value

    def peek(self) -> int:
        return self.my_stack[0]

    def empty(self) -> bool:
        return len(self.my_stack) == 0

# a = Solution();
# print(a.containsNearbyDuplicate([1,2,3,1,2,3], 2));
