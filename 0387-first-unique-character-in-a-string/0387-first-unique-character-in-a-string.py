from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        if len(count) == 1:
            tmp_list = list(count.items())
            if tmp_list[0][1] == 1:
                return 0
            return -1
        for index, char in enumerate(s):
            if count[char] == 1:
                return index

        return -1
