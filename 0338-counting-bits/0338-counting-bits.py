class Solution:
    def countBits(self, n: int) -> list[int]:
        result_arr = []
        for i in range(0, n+1, 1):
            binary = format(i, 'b')
            count = str(binary).count("1")
            result_arr.append(count)
        return result_arr