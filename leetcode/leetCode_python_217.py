class Solution(object):
    def containsDuplicate(self, nums: list[int]) -> bool:
        check_set = set()
        for value in nums:
            if value in check_set:
                return True
            else:
                check_set.add(value)
        return False


a = Solution();
print(a.containsDuplicate([1,2,3,1]));
