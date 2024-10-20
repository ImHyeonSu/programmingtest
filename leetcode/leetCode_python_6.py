class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = ""
        str_list = []
        process_count = 0
        process_flag = 1
        if numRows == 1:
            return s
        for i in range(numRows):
            str_list.append([])

        for var_s in s:
            if process_flag == 1 and process_count < numRows - 1:
                str_list[process_count].append(var_s)
                process_count += 1
            elif process_flag == -1 and process_count > 0:
                str_list[process_count].append(var_s)
                process_count -= 1
            elif process_flag == -1 and process_count == 0:
                str_list[process_count].append(var_s)
                process_flag = 1
                process_count += 1
            elif process_flag == 1 and process_count == numRows - 1:
                str_list[process_count].append(var_s)
                process_count -= 1
                process_flag = -1
        for list_var in str_list:
            result += "".join(list_var)
        return result


y = Solution()
print(y.convert("PAYPALISHIRING", 3))
