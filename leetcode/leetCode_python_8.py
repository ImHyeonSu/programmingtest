class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        minus_flag = False
        tmp_list = []
        result = 0
        list_str = "0123456789"
        if s[0] == "-":
            minus_flag = True
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
        for i in s:
            if len(tmp_list) == 0 and i == "0":
                continue
            if i in list_str:
                tmp_list.append(i)
            else:
                break
        tmp_result = "".join(tmp_list)
        if tmp_result:
            result = int(tmp_result)
        if minus_flag:
            result = result * -1
        if result < -(2**31):
            result = -(2**31)
        elif result > 2**31 - 1:
            result = 2**31 - 1

        return result


y = Solution()
print(y.myAtoi("42"))
