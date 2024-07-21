class Solution:
    def reverseVowels(self, s: str) -> str:
        index = []
        value = []
        list_s = list(s)
        check = set("aeiouAEIOU")
        for idx, val in enumerate(s):
            if val in check:
                index.append(idx)
                value.append(val)
        value.reverse()
        plus_num = 0
        for _, val_idx in enumerate(index):
            list_s[val_idx] = value[plus_num]
            plus_num += 1
        return "".join(list_s)


y = Solution()
print(y.reverseVowels("hello"))
