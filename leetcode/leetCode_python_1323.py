class Solution:
    def maximum69Number(self, num: int) -> int:
        max_num = num
        for i in range(len(str(num))):
            str_num = str(num)
            if str_num[i] == "6":
                str_num = str_num[:i] + "9" + str_num[i + 1 :]
            if int(str_num) > max_num:
                max_num = int(str_num)
        return max_num


y = Solution()
print(y.maximum69Number(9669))
