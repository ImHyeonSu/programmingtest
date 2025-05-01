class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_pos = {}
        for i, char in enumerate(s):
            last_pos[char] = i
        print(last_pos)
        result = []
        seen = set()
        for i, char in enumerate(s):
            if char in seen:
                continue
            while result and char < result[-1] and i < last_pos[result[-1]]:
                seen.remove(result.pop())
            result.append(char)
            seen.add(char)
        return "".join(result)


y = Solution()
print(y.removeDuplicateLetters("cbacdcbc"))
