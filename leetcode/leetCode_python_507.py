import math


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False

        sum_of_divisors = 1

        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                sum_of_divisors += i
                if i != num // i:
                    sum_of_divisors += num // i

        return sum_of_divisors == num
        # count = 0
        # for val in range(1, num // 2 + 1, 1):
        #     if num % val == 0:
        #         count += val
        # return count == num


y = Solution()
print(y.checkPerfectNumber(7))
