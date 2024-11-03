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
