class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        tmp_s = ""
        for i in s:
            if i == "#":
                if len(tmp_s) > 0:
                    tmp_s = tmp_s[0 : len(tmp_s) - 1]
                continue
            tmp_s += i
        tmp_t = ""
        for i in t:
            if i == "#":
                if len(tmp_t) > 0:
                    tmp_t = tmp_t[0 : len(tmp_t) - 1]
                continue
            tmp_t += i
        return tmp_s == tmp_t


y = Solution()
print(y.backspaceCompare("a#c", "b"))
