class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        return_list = []
        for num in range(left, right + 1):
            str_num = str(num)
            if "0" in str_num:
                continue
            for tmp_num in str_num:
                if num % int(tmp_num) != 0:
                    break
            else:
                return_list.append(num)
        return return_list