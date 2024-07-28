from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        counter1 = Counter(list(s))
        counter2 = Counter(list(t))

        diff = counter2 - counter1
        return list(diff.elements())[0]

y = Solution()
print(y.findTheDifference("a","aa"))
