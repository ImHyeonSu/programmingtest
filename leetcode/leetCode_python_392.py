class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        plus_num = 0
        for i in s:
            if t.find(i, index + plus_num) != -1 and index <= t.find(
                i, index + plus_num
            ):
                index = t.find(i, index + plus_num)
                plus_num = 1
            else:
                return False

        return True


y = Solution()
print(y.isSubsequence("abc", "ahbgdc"))
