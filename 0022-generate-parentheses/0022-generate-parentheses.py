class Solution:
    def generateParenthesis(self, n):
        result = []

        def backtrack(current_string, open_count, close_count, idx):
            if open_count == n and close_count == n:
                result.append(current_string)
                return

            if open_count < n:
                backtrack(current_string + "(", open_count + 1, close_count, idx + 1)

            if close_count < open_count:
                backtrack(current_string + ")", open_count, close_count + 1, idx + 1)

        backtrack("", 0, 0, 0)
        return result
