class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        result_dict = {}
        import string
        paragraph = paragraph.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation))).lower()

        for word in paragraph.split(" "):
            if word and word not in banned:
                result_dict[word] = result_dict.get(word, 0) + 1
        return max(result_dict, key=result_dict.get)
