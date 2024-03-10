class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        result_s = []
        result_t = []
        match_s = ""
        match_t = ""
        for index,_ in enumerate(s):
            if match_s != s[index]:
                match_s = s[index]
                result_s.append(1)
            else:
                result_s[len(result_s)-1] = result_s[len(result_s)-1] + 1
            if match_t != t[index]:
                match_t = t[index]
                result_t.append(1)
            else:
                result_t[len(result_t)-1] = result_t[len(result_t)-1] + 1
        if(len(result_s) != len(result_t)):
            return False
        else:
            for index,_ in enumerate(result_s):
                print(index)
                if result_s[index] != result_t[index]:
                    return False
        return True
a = Solution();
print(a.isIsomorphic("egg","stt"));
