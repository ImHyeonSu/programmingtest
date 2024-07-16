class NumArray:

    def __init__(self, nums: list[int]):
        self.prefix_sums = nums

    def sumRange(self, left: int, right: int) -> int:
        result = 0
        for i in range(left, right + 1, 1):
            result += self.prefix_sums[i]
        return result


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

y = NumArray([-2, 0, 3, -5, 2, -1])
print(y.sumRange(0, 5))
