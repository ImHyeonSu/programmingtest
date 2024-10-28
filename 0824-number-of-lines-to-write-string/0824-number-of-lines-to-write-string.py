class Solution:
    def numberOfLines(self, widths: list[int], s: str) -> list[int]:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        width_dict = {alphabet[i]: widths[i] for i in range(len(alphabet))}
        sum = 0
        row_count = 1
        for i in s:
            sum += width_dict[i]
            if sum == 100:
                sum = 0
                row_count += 1
            elif sum > 100:
                sum = 0
                sum += width_dict[i]
                row_count += 1
        if sum == 0:
            row_count -= 1
            sum = 100
        return [row_count, sum]