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


y = Solution()
print(
    y.numberOfLines(
[3,4,10,4,8,7,3,3,4,9,8,2,9,6,2,8,4,9,9,10,2,4,9,10,8,2],
        "mqblbtpvicqhbrejb",
    )
)
