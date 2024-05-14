class Solution:
    def isUgly(self, n: int) -> bool:
        while n >= 1:
            if n == 1:
                return True
            elif n%2 == 0:
                 n=n//2
            elif n%3 == 0:
                n=n//3
            elif n%5 == 0:
                n=n//5
            else:
                return False
        return False
        # def isUgly(num):
        #     if num <= 0:
        #         return False
        #     primes = [2, 3, 5]
        #     for prime in primes:
        #         while num % prime == 0:
        #             num //= prime
        #     return num == 1
a = Solution();
print(a.isUgly(-2147483648));
