# class Solution:
#     def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
#         return_list = []
#         min_num = max(len(list1), len(list2))
#         max_list = list1
#         min_list = list2
#         if min_num < len(list2):
#             max_list = list2
#             min_list = list1
#         for i, v in enumerate(max_list):
#             if v not in min_list:
#                 continue
#             tmp_num = i + min_list.index(v)

#             if tmp_num < min_num:
#                 min_num = tmp_num
#                 return_list = [v]
#             elif tmp_num == min_num:
#                 return_list.append(v)
#         return return_list


class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        index_sum = {}
        min_sum = float('inf')
        result = []

        for i, restaurant in enumerate(list1):
            index_sum[restaurant] = i

        for j, restaurant in enumerate(list2):
            if restaurant in index_sum:
                current_sum = index_sum[restaurant] + j
                if current_sum < min_sum:
                    min_sum = current_sum
                    result = [restaurant]
                elif current_sum == min_sum:
                    result.append(restaurant)
        
        return result

y = Solution()
print(
    y.findRestaurant(
        ["happy", "sad", "good"],
        ["sad", "happy", "good"],
    )
)
