class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        list_ransomNote = list(ransomNote)
        for var in magazine:
            if len(list_ransomNote) == 0:
                return True
            try:
                index = list_ransomNote.index(var)
                del list_ransomNote[index]
            except ValueError:
                continue
        if len(list_ransomNote) == 0:
            return True
        return False


y = Solution()
print(y.canConstruct("aab", "baa"))
