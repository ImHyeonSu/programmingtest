import string

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        upper_list = list(string.ascii_uppercase);
        
        title_len = len(columnTitle)
        
        if title_len == 1:
            return upper_list.index(columnTitle)+1
        result = 0

        for index,value in enumerate(columnTitle):
            result += (upper_list.index(value)+1) * 26 **(title_len-index-1)
        return result

        # AA 26 1 27 -> 
        # CC 26*3 3
        # ZY 26*26 25
        # ZZ 26*26 26 702
        # AAA  ->703


a = Solution()
print(a.titleToNumber("AAA"));