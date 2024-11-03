class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        max_list_len = max(len(nums1), len(nums2))
        long_list = nums1
        short_list = nums2
        result = list()
        if max_list_len < len(nums2):
            long_list = nums2
            short_list = nums1
        for index, val in enumerate(long_list):
            if val in short_list:
                delete_index = short_list.index(val)
                del short_list[delete_index]
                result.append(val)
        return result