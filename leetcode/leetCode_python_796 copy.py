class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        not_duplicate = set()
        morse_code_dict = {
            "a": ".-",
            "b": "-...",
            "c": "-.-.",
            "d": "-..",
            "e": ".",
            "f": "..-.",
            "g": "--.",
            "h": "....",
            "i": "..",
            "j": ".---",
            "k": "-.-",
            "l": ".-..",
            "m": "--",
            "n": "-.",
            "o": "---",
            "p": ".--.",
            "q": "--.-",
            "r": ".-.",
            "s": "...",
            "t": "-",
            "u": "..-",
            "v": "...-",
            "w": ".--",
            "x": "-..-",
            "y": "-.--",
            "z": "--..",
        }
        for word in words:
            morse_word = ""
            for word_str in word:
                morse_word += morse_code_dict[word_str]
            not_duplicate.add(morse_word)
        return len(not_duplicate)


y = Solution()
print(y.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
