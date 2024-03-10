class Solution:
    def isHappy(self, n: int) -> bool:
        result = 0
        result_list = []
        str_n = str(n)
        while len(str_n) >= 1:
            for v in str_n:
                result += int(v) ** 2
            if result in result_list:
                return False
            result_list.append(result)
            if result == 1:
                return True

            str_n = str(result)
            result = 0

a = Solution();
print(a.isHappy(2));
