class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        low = 0
        high = len(s)
        returnList = []

        for v in s:
            if v == "D":
                returnList.append(high)
                high -= 1
            else:
                returnList.append(low)
                low += 1
        returnList.append(low)

        return returnList


y = Solution()
print(y.diStringMatch("DDI"))
