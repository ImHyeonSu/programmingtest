# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         if s[::-1] == s:
#             return True
#         for i in range(0, len(s)):
#             tmp_s = s[:i] + s[i + 1 :]
#             if tmp_s[::-1] == tmp_s:
#                 return True
#         return False

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                return s[left+1:right+1] == s[left+1:right+1][::-1] or s[left:right] == s[left:right][::-1]
            left += 1
            right -= 1
        
        return True


y = Solution()
print(y.validPalindrome("abca"))
