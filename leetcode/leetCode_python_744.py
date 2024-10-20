# class Solution:
#     def nextGreatestLetter(self, letters: list[str], target: str) -> str:
#         if target in letters:
#             target_idx = letters.index(target)
#             for i in range(target_idx, len(letters)):
#                 if letters[i] != letters[target_idx]:
#                     return letters[i]
#         else:
#             for idx, letter in enumerate(letters):
#                 if ord(letter) > ord(target):
#                     return letters[idx]
#         return letters[0]


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        for letter in letters:
            if letter > target:
                return letter
        return letters[0]

y = Solution()
print(y.nextGreatestLetter(["e","e","e","e","e","e","n","n","n","n"], "e"))
