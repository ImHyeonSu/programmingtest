class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        five = 0
        ten = 0

        for bill in bills:
            if bill == 5:
                five += 1

            elif bill == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            else:  
                if ten >= 1 and five >= 1:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True


y = Solution()
print(y.lemonadeChange([5, 5, 10, 10, 20]))
# [5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]
