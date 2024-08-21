class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        if not timeSeries:
            return 0

        total_duration = 0
        end_time = 0

        for time in timeSeries:
            if time > end_time:
                total_duration += duration
            else:
                total_duration += time + duration - end_time

            end_time = time + duration
        return total_duration


y = Solution()
print(y.findPoisonedDuration([1, 2, 3, 4, 5], 5))
# 1 2 3 4 6
# [1, 2], 2
# [1,2,3,4,5,6,7,8,9] 1
# [1,2,3,4,5] 5
# [1,2,3,5] 2
