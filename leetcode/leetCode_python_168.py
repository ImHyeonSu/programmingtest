class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        test = columnNumber
        test2 = columnNumber
        real_result = ""
        while test > 0:
            test = test // 26
            test2 = test % 26
            if 1 <= test <= 26:  # 대문자 범위
                real_result = real_result + chr(test + ord("A") - 1)
            
            if test2 <= 26:
                real_result = real_result + chr(test + ord("A") - 1)
            test = test2
        return real_result


a = Solution()
print(a.convertToTitle(28))

# 703 = AAA
