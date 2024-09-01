class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        mul_num = abs(target - nums[0] + nums[1] + nums[2])
        for i in range(len(nums) - 2):
            first_num = nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                left_num = nums[left]
                right_num = nums[right]
                potentialSum = first_num + left_num + right_num
                tmp_mul = abs(target - potentialSum)
                if tmp_mul < mul_num:
                    result = potentialSum
                    mul_num = tmp_mul
                if potentialSum > target:
                    right -= 1
                elif potentialSum < target:
                    left += 1
                else:
                    return potentialSum
        return result


y = Solution()
print(y.threeSum([0, 1, 2], 3))
