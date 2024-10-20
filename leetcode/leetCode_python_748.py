import re
from collections import Counter


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        spell = "".join(re.findall(r"[a-zA-Z]", licensePlate)).lower()
        spell_counter = Counter(spell)
        return_str = None
        for word in words:
            word_counter = Counter(word.lower())
            if all(word_counter[char] >= spell_counter[char] for char in spell_counter):
                if return_str is None or len(word) < len(return_str):
                    return_str = word
        return return_str


y = Solution()
print(y.shortestCompletingWord("1s3 456", ["looks", "pest", "stew", "show"]))
