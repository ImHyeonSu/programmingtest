# class Solution:
#     def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
#         if len(flowerbed) == 1 and flowerbed[0] == 0 and n == 1:
#             return True
#         start_flower = 0
#         for i, v in enumerate(flowerbed):
#             if v == 1:
#                 start_flower = i + 1
#                 break
#         can_flower = len(flowerbed) // 2
#         if (start_flower == 0 or start_flower % 2 != 0) and len(flowerbed) % 2 != 0:
#             can_flower += 1
#         can_flower = can_flower - flowerbed.count(1)
#         if can_flower >= n:
#             return True
#         return False


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if (
                flowerbed[i] == 0
                and (i == 0 or flowerbed[i - 1] == 0)
                and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
            ):

                count += 1
                flowerbed[i] = 1
        return count >= n


y = Solution()
print(y.canPlaceFlowers([1, 0, 1, 0, 0, 1, 0], 1))
