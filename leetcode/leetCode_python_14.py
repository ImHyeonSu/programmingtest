class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        comman=""
        # returning "" , if  List is not present 
        if len(strs)==0:
            return comman

        # 0 to first_string length
        for i in range(len(strs[0])):
            print('test')
            print(i)
            for s in strs:
                if i==len(s) or s[i]!=strs[0][i]:
                    return comman
            comman+=strs[0][i]
            print(comman)
        return comman
    
s = Solution()
print(s.longestCommonPrefix(["owerfl","flow","flight"]))