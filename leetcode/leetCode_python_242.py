class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic = dict()
        t_dic = dict()
        for i in s:
            if i in s_dic:
                s_dic[i] = s_dic[i] +1
            else:
                s_dic[i] = 1
        for i in t:
            if i in t_dic:
                t_dic[i] = t_dic[i] +1
            else:
                t_dic[i] = 1        # for index in t:
        if(s_dic == t_dic):
            return True
        return False
a = Solution();
print(a.isAnagram("anagram","nagaram"));
