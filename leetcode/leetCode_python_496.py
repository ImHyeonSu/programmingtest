class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result_list = []
        for v in nums1:
            index = nums2.index(v)
            if index == len(nums2) - 1:
                result_list.append(-1)
            else:
                append_flag = False
                for tmp_idx in range(index, len(nums2)):
                    if nums2[tmp_idx] > nums2[index]:
                        result_list.append(nums2[tmp_idx])
                        append_flag = True
                        break
                if not append_flag:
                    result_list.append(-1)
        return result_list


y = Solution()
print(y.nextGreaterElement([4,1,2], [1,3,4,2]))
