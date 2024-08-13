class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 1:
            return False
        for i in range(len(s) // 2 + 1):
            if i == 0:
                continue
            else:
                repeat_str = s[0:i]
                repeat_count = 0
                result_count = len(s) // len(repeat_str)
                start_idx, end_idx = 0, len(repeat_str)
                while start_idx < len(s):
                    if repeat_str == s[start_idx:end_idx]:
                        start_idx += len(repeat_str)
                        end_idx += len(repeat_str)
                        repeat_count += 1
                    else:
                        break
                if result_count == repeat_count and s[start_idx:end_idx] == "" :
                    return True
        return False


y = Solution()
print(y.repeatedSubstringPattern("abcabcabcabc"))
