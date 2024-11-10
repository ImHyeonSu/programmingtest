class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        candidates.sort()

        def backtrack(remain, path, start):
            if remain == 0:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remain:
                    return
                path.append(candidates[i])
                backtrack(remain - candidates[i], path, i)
                path.pop()

        backtrack(target, [], 0)
        return result


a = Solution()
print(a.combinationSum([2, 3, 6, 7], 7))
