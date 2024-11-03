class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        return_word = ""
        for idx, word in enumerate(sentence.split(" ")):
            if word[0].lower() in ["a", "e", "i", "o", "u"]:
                word += "ma"
            else:
                word = word[1:] + word[0] + "ma"
            add_word = ""
            for _ in range(0, idx + 1, 1):
                add_word += "a"
            return_word += word + add_word + " "
        return return_word[0 : len(return_word) - 1]