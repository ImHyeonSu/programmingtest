class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        print(s)


y = Solution()
print(y.reverseString(["h", "e", "l", "l", "o"]))
