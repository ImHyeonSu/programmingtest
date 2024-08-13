class Solution:
    def arrangeCoins(self, n: int) -> int:
        tmp_list = []
        count = 1
        while n >= 1:
            if n - count > 0:
                tmp_list.append(count)
                n = n - count
            else:
                tmp_list.append(n)
                n = n - n
            count += 1

        if tmp_list[-1] == count - 1:
            return len(tmp_list)
        else:
            return len(tmp_list) - 1


y = Solution()
print(y.arrangeCoins(10))
