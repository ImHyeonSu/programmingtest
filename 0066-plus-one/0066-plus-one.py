class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        result = 0
        for i in range(0, len(digits)):
            result += digits[i] * (10 ** (len(digits) - i - 1))
        result += 1
        result_list = list(map(int, str(result)))
        return result_list