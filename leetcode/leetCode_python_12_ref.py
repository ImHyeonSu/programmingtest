class Solution:
    def intToRoman(self, num: int) -> str:
        val_to_roman = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        result = ""

        for value, roman in val_to_roman:
            while num >= value:
                result += roman
                num -= value

        return result


p = Solution()
print(p.intToRoman(1994))
# Output: "MMM DCC XL IX"
# MMM DCC XC IX
# MMM DCC XI IX
