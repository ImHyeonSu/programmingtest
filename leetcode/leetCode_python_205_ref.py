class Solution(object):
    def isIsomorphic(self, s, t):
        map1 = []
        map2 = []
        for idx in s:
            map1.append(s.index(idx))
            print(map1)
        for idx in t:
            map2.append(t.index(idx))
            print(map2)
        if map1 == map2:
            return True
        return False


a = Solution();
print(a.isIsomorphic("badc","baba"));
