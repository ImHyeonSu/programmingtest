class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        sorted_score = sorted(score, reverse=True)
        result_list = []
        score_dic = {}
        for idx, val in enumerate(sorted_score):
            if idx == 0:
                score_dic[val] = "Gold Medal"
            elif idx == 1:
                score_dic[val] = "Silver Medal"
            elif idx == 2:
                score_dic[val] = "Bronze Medal"
            else:
                score_dic[val] = str(idx + 1)
        for val in score:
            result_list.append(score_dic[val])

        return result_list


y = Solution()
print(y.findRelativeRanks([10, 3, 8, 9, 4]))
