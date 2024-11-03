class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        key_list = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        result = []
        for word in words:
            for index, value in enumerate(key_list):
                if word.lower()[0] in value:
                    key_index = index
            count = 0
            for tmp_str in word.lower():
                if tmp_str not in key_list[key_index]:
                    break
                else:
                    count += 1
            if count == len(word):
                result.append(word)
        return result