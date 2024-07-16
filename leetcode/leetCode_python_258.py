class Solution:
    def addDigits(self, num: int) -> int:
        # loop
        while len(str(num)) > 1:
            # 条件
            return_num = 0
            for value in str(num):
                return_num += int(value)
            num = return_num
        # return
        return num


a = Solution();
print(a.addDigits(38));
