class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = len(nums)
        mid = (n + 1) // 2
        small = nums[:mid]
        small.reverse()
        big = nums[mid:]
        big.reverse()
        for i in range(n):
            if i % 2 == 0:
                nums[i] = small[i // 2]
            else:
                nums[i] = big[i // 2]
        return nums


y = Solution()
# print(y.wiggleSort([1, 5, 1, 1, 6, 4]))
print(y.wiggleSort([1, 3, 2, 2, 3, 1]))
# [1, 1, 2], [2, 3, 3]
