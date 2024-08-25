class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        word_flag = 0
        result = True
        if word[0].islower():
            word_flag = 1
        if word[0].isupper() and word[1].islower():
            word_flag = 2
        for index, val in enumerate(word):
            if word_flag == 0:
                if val.isupper():
                    continue
                else:
                    result = False
                    break
            if word_flag == 1:
                if val.islower():
                    continue
                else:
                    result = False
                    break
            if word_flag == 2:
                if index == 0:
                    continue
                if val.islower():
                    continue
                else:
                    result = False
                    break
        return result


y = Solution()
print(y.detectCapitalUse("Google"))
