class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result_list = []
        for v in nums1:
            index = nums2.index(v)
            next_greater = -1
            for i in range(index + 1, len(nums2)):
                if nums2[i] > v:
                    next_greater = nums2[i]
                    break
            result_list.append(next_greater)
        return result_list