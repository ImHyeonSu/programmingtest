class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        indices = [i for i, char in enumerate(s) if char == c]
        result = []
        for i in range(len(s)):
            min_distance = min(abs(i - idx) for idx in indices)
            result.append(min_distance)
            
        return result