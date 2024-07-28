class Solution:
    def firstUniqChar(self, s: str) -> int:
        result = 0
        for index, value in enumerate(s):
            tmp_index = s.count(value)
            if tmp_index == 1:
                return index
            else:
                if tmp_index == len(s):
                    return -1
                continue

        return -1


y = Solution()
print(y.firstUniqChar("aabb"))
