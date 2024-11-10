class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        candidates.sort()

        def backtrack(remain, path, start):
            if remain == 0:
                if path[:] not in result:
                    result.append(path[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > remain:
                    break
                path.append(candidates[i])
                backtrack(remain - candidates[i], path, i + 1)
                path.pop()

        backtrack(target, [], 0)
        return result


a = Solution()
print(a.combinationSum2([2, 5, 2, 1, 2], 5))
