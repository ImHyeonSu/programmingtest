# class Solution:
#     def canThreePartsEqualSum(self, arr: list[int]) -> bool:
#         divided_total = sum(arr) // 3
#         mock_arr = []
#         result_mock_arr = []
#         for i in arr:
#             mock_arr.append(i)
#             if sum(mock_arr) == divided_total:
#                 result_mock_arr.append(mock_arr)
#                 mock_arr = []
#         return len(result_mock_arr) == 3


class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        total = sum(arr)

        if total % 3 != 0:
            return False

        target = total // 3
        current_sum = 0
        count = 0

        for i in range(len(arr) - 1):
            current_sum += arr[i]

            if current_sum == target:
                count += 1
                current_sum = 0

                if count == 2:
                    return True

        return False


y = Solution()
print(y.canThreePartsEqualSum([0, 0, 0, 0]))
