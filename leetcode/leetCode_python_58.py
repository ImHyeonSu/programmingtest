class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        count = 0
        if len(s) == 1 and s != " ":
            return 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                break
            count += 1
        return count


a = Solution()
print(a.lengthOfLastWord("    day"))
