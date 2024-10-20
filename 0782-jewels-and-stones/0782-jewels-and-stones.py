class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return_count = 0
        for i in stones:
            if i in jewels:
                return_count += 1
        return return_count
