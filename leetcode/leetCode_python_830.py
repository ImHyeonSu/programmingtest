class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        last_word = ""
        start_idx = 0
        return_list = []
        for idx, v in enumerate(s):
            if v != last_word:
                last_word = v
                if idx - start_idx >= 3:
                    return_list.append([start_idx, idx - 1])
                start_idx = idx
        if len(s) - start_idx >= 3:
            return_list.append([start_idx, len(s) - 1])
        return return_list


y = Solution()
print(y.largeGroupPositions("aaa"))
