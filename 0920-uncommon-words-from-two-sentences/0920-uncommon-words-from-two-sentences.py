class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        result = []
        split_s1 = s1.split(" ")
        split_s2 = s2.split(" ")
        for tmp_s1 in split_s1:
            if split_s1.count(tmp_s1) > 1 or tmp_s1 in split_s2:
                continue
            result.append(tmp_s1)
        for tmp_s2 in split_s2:
            if split_s2.count(tmp_s2) > 1 or tmp_s2 in split_s1:
                continue
            result.append(tmp_s2)
        return result