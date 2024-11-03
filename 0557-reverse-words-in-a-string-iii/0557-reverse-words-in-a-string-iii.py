class Solution:
    def reverseWords(self, s: str) -> str:
        tmp_s = ""
        tmp_str = ""
        start_line = 0
        for i in range(0, len(s)):
            if s[i] == " ":
                tmp_str = s[start_line:i]
                if start_line != 0:
                    tmp_s += " "
                tmp_s += tmp_str[::-1].strip()
                start_line = i
        tmp_str = s[start_line : len(s)]
        tmp_s += " "
        tmp_s += tmp_str[::-1]
        return tmp_s.strip()