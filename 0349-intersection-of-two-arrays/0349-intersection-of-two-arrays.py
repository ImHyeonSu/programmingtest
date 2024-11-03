class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        max_list_len = max(len(nums1), len(nums2))
        long_list = nums1
        short_list = nums2
        result = set()
        if max_list_len < len(nums2):
            long_list = nums2
            short_list = nums1
        for val in long_list:
            if val in short_list:
                result.add(val)
        return list(result)