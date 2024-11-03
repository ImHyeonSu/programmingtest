class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0
        lastnum = 0
        for i in s:
            if lastnum < dic[i] and result != 0 :
                lastnum = dic[i] - (2*lastnum)
            else:
                lastnum = dic[i]
            result += lastnum
        return result