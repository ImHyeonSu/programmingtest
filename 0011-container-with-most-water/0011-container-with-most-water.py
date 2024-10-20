class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_length = 0
        left, right = 0, len(height) - 1

        while left < right:
            width = right - left
            height_container = min(height[left], height[right])
            max_length = max(max_length, width * height_container)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_length