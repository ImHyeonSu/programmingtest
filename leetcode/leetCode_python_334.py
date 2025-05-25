class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = float("inf")
        second = float("inf")
        for num in nums:
            print(first, second)
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False


y = Solution()
print(y.increasingTriplet([2, 1, 5, 0, 4, 6]))
