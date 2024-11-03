class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list_s = s.split(" ")
        tmp_dict = {}
        if len(pattern) != len(list_s):
            return False
        for i, v in enumerate(pattern):
            if v not in tmp_dict:
                tmp_dict[v] = [list_s[i]]
            else:
                if tmp_dict[v][0] == list_s[i]:
                    continue
                else:
                    tmp_dict[v].append(list_s[i])
        for i in tmp_dict:
            if len(tmp_dict[i]) > 1:
                return False
        keys_list = list(tmp_dict.keys())
        key_len = 0
        while key_len < len(keys_list) - 1:
            value = tmp_dict[keys_list[key_len]]
            for key, value2 in tmp_dict.items():
                if key != keys_list[key_len] and value == value2:
                    return False
            key_len += 1
        return True
