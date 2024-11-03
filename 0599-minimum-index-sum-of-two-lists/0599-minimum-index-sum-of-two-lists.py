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