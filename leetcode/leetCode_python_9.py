class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x > 0:
            num_list = list(map(int,str(x)))
        elif x == 0:
            return True
        else:
            return False
        back_numlist = num_list[::-1]

        for i in range(len(num_list)):
            if num_list[i] == back_numlist[i]:
                continue
            else:
                return False
        return True
    

y = Solution()
print(y.isPalindrome(10))
