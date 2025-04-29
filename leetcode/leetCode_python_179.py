# class Solution:
#     def largestNumber(self, nums: list[int]) -> str:
#         nums_str = [str(num) for num in nums]
#         n = len(nums_str)
#         for i in range(n):
#             for j in range(0, n - i - 1):
#                 if nums_str[j] + nums_str[j + 1] < nums_str[j + 1] + nums_str[j]:
#                     nums_str[j], nums_str[j + 1] = nums_str[j + 1], nums_str[j]
#         result = "".join(nums_str)
#         return "0" if result[0] == "0" else result


class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        # 정렬을 위한 특별한 비교 클래스 정의
        class LargerNumKey(str):
            def __lt__(self, other):
                print(self, other)
                return self + other > other + self

        # 문자열로 변환 후 정렬
        nums_str = [str(num) for num in nums]
        nums_str.sort(key=LargerNumKey)

        # 결과 문자열 생성 (모든 숫자가 0인 경우 처리)
        result = "".join(nums_str)
        return "0" if result[0] == "0" else result


a = Solution()
# 9 5 34 3 30
print(a.largestNumber([3, 30, 34, 5, 9]))
