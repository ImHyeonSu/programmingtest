class Solution:
    def hammingWeight(self, n: int) -> int:
        # Initialize a counter variable to 0
        count = 0
        # Loop until n is 0
        while n != 0:
            # If the last bit of n is 1, increment the counter
            if n & 1 == 1:
                count += 1
            # Shift n to the right by 1 bit
            n = n >> 1
        # Return the counter
        return count

# 반드시 11 이라치면 8을간뒤에 4를가는 식으로 코드를 구성해야할듯
# 11 2*e3 + 2*e1 + 1  17  2*e4 + 1


a = Solution()
print(a.hammingWeight(11))
