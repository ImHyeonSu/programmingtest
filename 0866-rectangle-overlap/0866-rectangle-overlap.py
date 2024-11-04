class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        if rec1[2] <= rec2[0] or rec2[2] <= rec1[0]:
            return False
        if rec1[0] >= rec2[2] or rec2[0] >= rec1[2]:
            return False
        if rec1[3] <= rec2[1] or rec2[3] <= rec1[1]:
            return False
        if rec1[1] >= rec2[3] or rec2[1] >= rec1[3]:
            return False
        return True
