class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        total = sum(arr)

        if total % 3 != 0:
            return False

        target = total // 3
        current_sum = 0
        count = 0

        for i in range(len(arr) - 1):
            current_sum += arr[i]

            if current_sum == target:
                count += 1
                current_sum = 0

                if count == 2:
                    return True

        return False