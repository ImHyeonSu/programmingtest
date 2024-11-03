from collections import Counter


class Solution:
    def checkRecord(self, s: str) -> bool:
        counter = Counter(s)
        tmp_list = []
        if counter["A"] >= 2:
            return False
        if counter["L"] >= 3:
            for i in range(0, len(s)):
                if s[i] == "L":
                    tmp_list.append(i)
            tmp_val = 0
            tmp_count = 0
            for val in tmp_list:
                if tmp_val + 1 == val:
                    tmp_count += 1
                else:
                    tmp_count = 1
                tmp_val = val
                if tmp_count == 3:
                    return False
        return True