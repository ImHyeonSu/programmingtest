class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        result = []
        before_size = 0
        if area == 1:
            return [1, 1]
        for i in range(1, area):
            if area % i == 0:
                tmp_num = area // i
                if i == 1 or before_size >= max(i, tmp_num) - min(i, tmp_num):
                    before_size = max(i, tmp_num) - min(i, tmp_num)
                    result = [max(i, tmp_num), min(i, tmp_num)]
        return result


y = Solution()
print(y.constructRectangle())
