class Solution:
    def calPoints(self, operations: list[str]) -> int:
        return_list = []
        for data in operations:
            if data == "C":
                if len(return_list) > 0:
                    return_list.pop()
                continue
            if data == "D":
                if len(return_list) > 0:
                    return_list.append(return_list[len(return_list) - 1] * 2)
                continue
            if data == "+":
                if len(return_list) > 1:
                    return_list.append(
                        return_list[len(return_list) - 1]
                        + return_list[len(return_list) - 2]
                    )
                continue
            int_data = int(data)
            return_list.append(int_data)

        return sum(return_list)