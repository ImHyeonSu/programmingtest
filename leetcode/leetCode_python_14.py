class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        comman = ""
        # returning "" , if  List is not present
        if len(strs) == 0:
            return comman

        # 0 to first_string length
        for i in range(len(strs[0])):
            for s in strs:
                # if条件１、比較するためのindex iとsの長さが同じ場合比較不可能になってるのでreturn
                # if条件２、sのiの文字と比較対象のiの文字が同じじゃない場合return
                if i == len(s) or s[i] != strs[0][i]:
                    return comman
            comman += strs[0][i]
        return comman


s = Solution()
print(s.longestCommonPrefix(["ab", "a"]))
