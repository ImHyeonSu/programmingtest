class Solution:
    def findComplement(self, num: int) -> int:
        binaryNum = format(num, "b")
        result = ""
        for i in binaryNum:
            if i == "1":
                result += "0"
            else:
                result += "1"
        return int(result, 2)


y = Solution()
print(y.findComplement(1))
