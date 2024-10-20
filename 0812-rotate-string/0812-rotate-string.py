class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(0, len(s)):
            s = s[1 : len(s)] + s[0]
            if s == goal:
                return True
        return False