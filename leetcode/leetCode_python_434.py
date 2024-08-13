class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())


y = Solution()
print(y.countSegments("Hello"))
