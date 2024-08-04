from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        ans = 0
        for key, i in c.items():
            ans += int(i / 2) * 2
            if ans % 2 == 0 and i % 2 == 1:
                ans += 1
        return ans
        # if len(s) <= 1:
        #     return len(s)
        # counter_list = Counter(s)
        # one_flag = False
        # result = 0
        # if len(counter_list) == 1:
        #     return list(counter_list.items())[0][1]
        # for key, value in counter_list.items():
        #     if value % 2 == 0:
        #         result += value
        #     else:
        #         if value != 1 and (value - 1) % 2 == 0:
        #             # print(key, value)
        #             if value != 1:
        #                 result += value - 1
        #         elif value == 1:
        #             one_flag = True
        # if one_flag == True:
        #     result += 1
        # return result
        # 983


y = Solution()
print(y.longestPalindrome("ababababa"))
