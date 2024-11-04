class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        abc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ans=""
        while columnNumber:
            columnNumber = columnNumber-1
            ans = abc[columnNumber % 26]+ans
            columnNumber = columnNumber//26
        return ans


a = Solution()
print(a.convertToTitle(28))

# 703 = AAA
